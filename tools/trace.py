#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Build the trace matrix and the coverage report from the spec.

Reads
  spec/**/*.md                      YAML front-matter of stories, system stories, ADRs, ...
  spec/20-requirements/requirements.md
                                    requirement rows: REQ-### | quadrant | sentence | sources | KYIV | links [| vN] [| status]
                                    (a row defines a REQ only when its 2nd cell is S-F, S-NF, U-F or U-NF)
  spec/30-stories/epics.md          EP-## and FT-##.# rows; the REQ ids in an FT row are that feature's members
  spec/01-context, 10-design, CHANGELOG.md
                                    ids (CTX, Q, A, CF, ADR, CR) defined at the start of a line or table row
  spec/40-tasks/tasks.yaml          list of tasks
  spec/00-inputs/_extracted/*.md    source register (type: source)

Writes (GENERATED, never edit by hand)
  spec/90-trace/trace.csv, spec/90-trace/coverage-report.md, traces_to lines in spec/40-tasks/tasks.yaml

Usage
  uv run tools/trace.py             # or python3 tools/trace.py with PyYAML installed
  uv run tools/trace.py --check     # write nothing; also fail if generated files are out of date

Exit code 1 when a K item has a coverage gap, an ID is duplicated, or a file cannot be parsed.
"""
import argparse
import csv
import io
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing: run `uv run tools/trace.py`, or `pip install pyyaml` first.")

RANK = {"K": 4, "Y": 3, "I": 2, "V": 1}
MATURITY = ["deprecated", "draft", "in-review", "approved"]
QUADRANTS = ["S-F", "S-NF", "U-F", "U-NF"]
STORY_TYPES = {"user-story", "job-story"}
REQUIRED_FIELDS = ["id", "type", "title", "status", "owner", "version", "kyiv", "sources"]

ID_RE = re.compile(
    r"\b(?:SRC-[A-Z]+\d+|REQ-\d{3,}|US-\d{3,}|JS-\d{3,}|SS-\d{3,}|T-\d{3,}|EP-\d{2,}|FT-\d{2,}\.\d+"
    r"|CTX-\d{3,}|Q-\d{3,}|A-\d{3,}|CF-\d{3,}|ADR-\d{3,}|CR-\d{3,})\b"
)
LINE_DEF_RE = re.compile(r"^[\s>|#*\-]*[*`]*(" + ID_RE.pattern + r")")
# Where an ID starting a line or table row counts as its definition (folder or file name -> prefixes).
DEFINED_IN = {"01-context": ("CTX-", "Q-", "A-", "CF-"), "adr": ("ADR-",),
              "epics.md": ("EP-", "FT-"), "CHANGELOG.md": ("CR-",)}


def natural(s: str):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", s)]


def as_int(v, default=1) -> int:
    m = re.search(r"\d+", str(v if v is not None else ""))
    return int(m.group()) if m else default


def as_list(v) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def ids(v) -> list:
    """All spec IDs mentioned in a front-matter value (list, string or mapping keys)."""
    if isinstance(v, dict):
        v = list(v)
    return [m for item in as_list(v) for m in ID_RE.findall(str(item))]


def norm_kyiv(v):
    if v is True:  # unquoted Y/yes in YAML 1.1
        return "Y"
    s = str(v or "").strip().upper()
    return s if s in RANK else None


def split_row(line: str) -> list:
    s = line.strip()
    if "|" not in s:
        return []
    s = s.strip("|")
    return [re.sub(r"[*`]", "", c).strip() for c in re.split(r"(?<!\\)\|", s)]


class Spec:
    def __init__(self, root: Path):
        self.root = root
        self.spec = root / "spec"
        self.items = {}       # id -> record (chain artefacts and ADRs)
        self.defined = set()  # every id defined anywhere
        self.sources = {}     # SRC id -> extract file
        self.features = {}    # FT id -> set of REQ ids
        self.duplicates = []
        self.problems = []
        self.tasks_text = None
        self.load()

    # ---------- loading ----------

    def rel(self, path: Path) -> str:
        return str(path.relative_to(self.root))

    def add(self, rec: dict):
        if rec["id"] in self.items:
            self.duplicates.append((rec["id"], self.items[rec["id"]]["file"], rec["file"]))
            return
        self.items[rec["id"]] = rec
        self.defined.add(rec["id"])

    def record(self, data: dict, file: str) -> dict:
        return {
            "id": str(data["id"]),
            "type": str(data.get("type") or ""),
            "title": str(data.get("title") or ""),
            "status": str(data.get("status") or "draft"),
            "version": as_int(data.get("version")),
            "kyiv": norm_kyiv(data.get("kyiv")),
            "override": data.get("kyiv_override_reason"),
            "parents": ids(data.get("parents")),
            "requirements": ids(data.get("requirements")),
            "implements": ids(data.get("implements")),
            "depends_on": ids(data.get("depends_on")),
            "blocks": ids(data.get("blocks")),
            "epic": str(data.get("epic") or ""),
            "feature": str(data.get("feature") or ""),
            "sources": [str(s) for s in as_list(data.get("sources"))],
            "approved_with": data.get("approved_with") or {},
            "has_traces_to": "traces_to" in data,
            "file": file,
            "raw": data,
        }

    def front_matter(self, path: Path):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None, text
        m = re.search(r"^---\s*$", text[3:], re.M)
        if not m:
            raise ValueError("front-matter is not closed with ---")
        data = yaml.safe_load(text[3:3 + m.start()]) or {}
        if not isinstance(data, dict):
            raise ValueError("front-matter is not a mapping")
        return data, text[3 + m.end():]

    def load(self):
        for path in sorted(self.spec.rglob("*.md")):
            parts = path.relative_to(self.spec).parts
            if parts[0] == "90-trace" or (parts[0] == "00-inputs" and "_extracted" not in parts):
                continue
            try:
                data, body = self.front_matter(path)
            except Exception as e:  # noqa: BLE001 - report and keep going
                self.problems.append((self.rel(path), f"front-matter: {e}"))
                continue
            data = data or {}
            if data.get("type") == "source":
                self.sources[str(data["id"])] = self.rel(path)
                self.defined.add(str(data["id"]))
                continue
            if parts[0] == "00-inputs":
                continue
            if data.get("id") and data.get("type") in STORY_TYPES | {"system-story", "adr"}:
                self.add(self.record(data, self.rel(path)))
            elif data.get("id"):
                self.defined.add(str(data["id"]))
            if path.name == "requirements.md":
                self.parse_requirements(body, data, self.rel(path))
            elif path.name == "epics.md":
                self.parse_epics(body)
            for where, prefixes in DEFINED_IN.items():
                if where in parts:
                    self.parse_line_defs(body, prefixes)
        self.load_tasks()

    def parse_line_defs(self, body: str, prefixes: tuple):
        for line in body.splitlines():
            m = LINE_DEF_RE.match(line)
            if m and m.group(1).startswith(prefixes):
                self.defined.add(m.group(1))

    def parse_requirements(self, body: str, data: dict, file: str):
        file_status = str(data.get("status") or "draft")
        section = ""
        for n, line in enumerate(body.splitlines(), start=1):
            h = re.match(r"^#+\s*(.*)", line)
            if h:
                section = h.group(1).lower()
                continue
            cells = split_row(line)
            if len(cells) < 2 or not re.fullmatch(r"REQ-\d{3,}", cells[0]) or cells[1] not in QUADRANTS:
                continue
            if len(cells) < 5:
                self.problems.append((file, f"{cells[0]}: expected at least 5 cells, got {len(cells)}"))
                continue
            kyiv = re.search(r"\b([KYIV])\b", cells[4].replace("KYIV", ""))
            version = re.search(r"\d+", cells[6]) if len(cells) > 6 else None
            status = cells[7].lower() if len(cells) > 7 and cells[7].lower() in MATURITY else file_status
            self.add({
                **self.record({"id": cells[0], "type": "requirement", "title": cells[2], "status": status,
                               "version": int(version.group()) if version else 1}, f"{file}:{n}"),
                "kyiv": kyiv.group(1) if kyiv else None,
                "kyiv_final": "final" in cells[4].lower(),
                "quadrant": cells[1],
                "sources": ID_RE.findall(cells[3]),
                "links": ID_RE.findall(cells[5]) if len(cells) > 5 else [],
                "parked": "parking" in section,
            })

    def parse_epics(self, body: str):
        for line in body.splitlines():
            cells = split_row(line)
            if cells and re.fullmatch(r"FT-\d{2,}\.\d+", cells[0]):
                self.features.setdefault(cells[0], set()).update(
                    i for c in cells[1:] for i in ID_RE.findall(c) if i.startswith("REQ-"))

    def load_tasks(self):
        path = self.spec / "40-tasks" / "tasks.yaml"
        if not path.exists():
            return
        self.tasks_text = path.read_text(encoding="utf-8")
        try:
            data = yaml.safe_load(self.tasks_text) or []
        except yaml.YAMLError as e:
            self.problems.append((self.rel(path), f"yaml: {e}"))
            return
        if isinstance(data, dict):
            data = data.get("tasks") or []
        for t in data:
            if not isinstance(t, dict) or not t.get("id"):
                self.problems.append((self.rel(path), f"task without id: {str(t)[:60]}"))
                continue
            self.add(self.record({**t, "type": "task"}, self.rel(path)))

    # ---------- graph ----------

    def of_type(self, *types) -> dict:
        return {i: r for i, r in self.items.items() if r["type"] in types}

    def parent_ids(self, r: dict) -> list:
        """Links one level up the chain: story -> REQ, SS -> story + REQ, task -> SS."""
        if r["type"] in STORY_TYPES:
            return sorted(set(r["requirements"] + [p for p in r["parents"] if p.startswith("REQ-")]), key=natural)
        if r["type"] == "system-story":
            return sorted(set(r["parents"] + r["requirements"]), key=natural)
        if r["type"] == "task":
            return r["implements"]
        return []

    def story_reqs(self, r: dict) -> set:
        return set(r["requirements"] + [p for p in r["parents"] if p.startswith("REQ-")])

    def ss_stories(self, r: dict) -> set:
        return {p for p in r["parents"] if p.startswith(("US-", "JS-"))}

    def effective_kyiv(self, r: dict, seen=()):
        if r["kyiv"]:
            return r["kyiv"]
        found = [self.effective_kyiv(self.items[p], seen + (r["id"],))
                 for p in self.parent_ids(r) if p in self.items and p not in seen]
        found = [k for k in found if k]
        return max(found, key=RANK.get) if found else None

    def epic_of_req(self, req_id: str) -> str:
        for ft, members in sorted(self.features.items()):
            if req_id in members:
                return "EP-" + ft[3:].split(".")[0]
        return ""


def analyse(s: Spec) -> dict:
    reqs = s.of_type("requirement")
    stories = s.of_type(*STORY_TYPES)
    sss = s.of_type("system-story")
    tasks = s.of_type("task")
    active = lambda r: r["status"] != "deprecated"  # noqa: E731

    covered = set()
    for st in filter(active, stories.values()):
        covered |= s.story_reqs(st)
    for ss in filter(active, sss.values()):
        if not s.ss_stories(ss):  # enabler: links straight to REQ
            covered |= set(ss["requirements"])
    ss_of_story = {i: [ss["id"] for ss in sss.values() if active(ss) and i in s.ss_stories(ss)] for i in stories}
    tasks_of_ss = {i: [t["id"] for t in tasks.values() if active(t) and i in t["implements"]] for i in sss}
    traces_to = {t: sorted({q for ss in r["implements"] if ss in sss for q in sss[ss]["requirements"]}, key=natural)
                 for t, r in tasks.items()}

    res = {"reqs": reqs, "stories": stories, "sss": sss, "tasks": tasks, "traces_to": traces_to,
           "ss_of_story": ss_of_story, "tasks_of_ss": tasks_of_ss}
    res["req_no_story"] = [r for r in reqs.values() if active(r) and r["kyiv"] != "V" and r["id"] not in covered]
    res["parked_no_story"] = [r for r in reqs.values() if active(r) and r["kyiv"] == "V" and r["id"] not in covered]
    res["story_no_ss"] = [r for i, r in stories.items() if active(r) and not ss_of_story[i]]
    res["ss_no_task"] = [r for i, r in sss.items() if active(r) and not tasks_of_ss[i]]
    res["task_no_req"] = [r for i, r in tasks.items() if active(r) and not traces_to[i]]
    res["no_source"] = [r for r in s.items.values()
                        if r["type"] != "task" and active(r) and not any(i.startswith(("SRC-", "CTX-")) for i in ids(r["sources"]))]

    # dangling references
    dangling = []
    for r in s.items.values():
        refs = {"parents": r["parents"], "requirements": r["requirements"], "implements": r["implements"],
                "depends_on": r["depends_on"], "blocks": r["blocks"], "sources": ids(r["sources"]),
                "approved_with": ids(r["approved_with"]), "links": r.get("links", []),
                "epic": ids(r["epic"]), "feature": ids(r["feature"])}
        for field, vals in refs.items():
            dangling += [(r, field, v) for v in vals if v not in s.defined]
    for ft, members in s.features.items():
        dangling += [({"id": ft, "file": "spec/30-stories/epics.md"}, "members", m) for m in members if m not in reqs]
    res["dangling"] = dangling

    # front-matter completeness for chain artefacts kept in .md files
    fm_problems = []
    for r in list(stories.values()) + list(sss.values()):
        missing = [f for f in REQUIRED_FIELDS if f not in r["raw"]]
        if not r["requirements"]:
            missing.append("requirements")
        if r["type"] == "system-story" and "parents" not in r["raw"]:
            missing.append("parents")
        if r["status"] not in MATURITY:
            fm_problems.append((r, f"unknown status '{r['status']}'"))
        if missing:
            fm_problems.append((r, "missing " + ", ".join(missing)))
    for r in tasks.values():
        if not r["has_traces_to"]:
            fm_problems.append((r, "missing traces_to line (trace.py fills it, but the key must exist)"))
    res["fm_problems"] = fm_problems

    # features: each requirement belongs to exactly one
    feat = []
    if s.features:
        for r in filter(active, reqs.values()):
            n = sum(r["id"] in m for m in s.features.values())
            if n != 1:
                feat.append((r, "in no feature" if n == 0 else f"in {n} features"))
    res["features"] = feat

    # priority
    missing_kyiv, conflicts, mismatches, overrides = [], [], [], []
    for r in s.items.values():
        if r["type"] not in STORY_TYPES | {"system-story", "task"} or not active(r):
            continue
        parent_k = [s.effective_kyiv(s.items[p]) for p in s.parent_ids(r) if p in s.items]
        parent_k = [k for k in parent_k if k]
        if not r["kyiv"]:
            missing_kyiv.append(r)
        if not parent_k or not r["kyiv"]:
            continue
        expected = max(parent_k, key=RANK.get)
        if RANK[r["kyiv"]] > RANK[expected]:
            conflicts.append((r, expected))
        elif r["kyiv"] != expected:
            (overrides if r["override"] else mismatches).append((r, expected))
    missing_kyiv += [r for r in reqs.values() if active(r) and not r["kyiv"]]
    res.update(missing_kyiv=missing_kyiv, conflicts=conflicts, mismatches=mismatches, overrides=overrides)

    # staleness: approved artefacts stamp the parent versions they were approved against
    stale, unstamped = [], []
    for r in s.items.values():
        if r["status"] != "approved" or r["type"] not in STORY_TYPES | {"system-story", "task"}:
            continue
        stamp = {str(k): v for k, v in (r["approved_with"] or {}).items()}
        parents = [p for p in s.parent_ids(r) if p in s.items]
        missing = [p for p in parents if p not in stamp]
        if missing:
            unstamped.append((r, missing))
        for p in parents:
            if p in stamp and s.items[p]["version"] > as_int(stamp[p]):
                stale.append((r, p, as_int(stamp[p]), s.items[p]["version"]))
    res.update(stale=stale, unstamped=unstamped)

    # task dependency graph
    cycles, mismatched = [], []
    graph = {i: [d for d in r["depends_on"] if d in tasks] for i, r in tasks.items()}
    state = {}

    def visit(node, path):
        state[node] = 1
        for d in graph[node]:
            if state.get(d) == 1:
                cycles.append(path[path.index(d):] + [d] if d in path else [node, d])
            elif not state.get(d):
                visit(d, path + [d])
        state[node] = 2

    for i in sorted(graph, key=natural):
        if not state.get(i):
            visit(i, [i])
    for i, r in tasks.items():
        mismatched += [(i, b) for b in r["blocks"] if b in tasks and i not in tasks[b]["depends_on"]]
        mismatched += [(d, i) for d in r["depends_on"] if d in tasks and i not in tasks[d]["blocks"]]
    res.update(cycles=cycles, block_mismatch=sorted(set(mismatched), key=lambda x: natural(x[0] + x[1])))

    # K gaps decide the exit code
    gap_lists = ["req_no_story", "story_no_ss", "ss_no_task", "task_no_req"]
    res["k_gaps"] = [(name, r) for name in gap_lists for r in res[name] if s.effective_kyiv(r) == "K"]
    return res


# ---------- outputs ----------

def trace_rows(s: Spec, res: dict) -> list:
    stories, sss, tasks = res["stories"], res["sss"], res["tasks"]
    rows, seen = [], set()

    def status(*recs):
        recs = [r for r in recs if r]
        return min((r["status"] for r in recs), key=lambda x: MATURITY.index(x) if x in MATURITY else 0)

    def emit(req, story, ss):
        task_ids = res["tasks_of_ss"].get(ss["id"], []) if ss else []
        for t in task_ids or [None]:
            task = tasks.get(t) if t else None
            epic = (s.epic_of_req(req["id"]) if req else "") or next(
                (r["epic"] for r in (story, ss, task) if r and r["epic"]), "")
            rows.append([req["id"] if req else "", req.get("quadrant", "") if req else "",
                         (req["kyiv"] or "") if req else "", story["id"] if story else "", ss["id"] if ss else "",
                         t or "", epic, status(req, story, ss, task)])
            seen.update(x["id"] for x in (req, story, ss, task) if x)

    for rid in sorted(res["reqs"], key=natural):
        req = res["reqs"][rid]
        linked = [st for st in stories.values() if rid in s.story_reqs(st)]
        enablers = [ss for ss in sss.values() if not s.ss_stories(ss) and rid in ss["requirements"]]
        if not linked and not enablers:
            emit(req, None, None)
        for st in sorted(linked, key=lambda r: natural(r["id"])):
            under = [sss[i] for i in res["ss_of_story"][st["id"]] if rid in sss[i]["requirements"] or not sss[i]["requirements"]]
            for ss in sorted(under, key=lambda r: natural(r["id"])) or [None]:
                emit(req, st, ss)
        for ss in sorted(enablers, key=lambda r: natural(r["id"])):
            emit(req, None, ss)
    # orphans: anything not reached from a requirement still gets a row
    for i in sorted(set(stories) | set(sss) | set(tasks), key=natural):
        if i in seen:
            continue
        r = s.items[i]
        if r["type"] == "task":
            rows.append(["", "", "", "", "", i, r["epic"], status(r)])
        elif r["type"] == "system-story":
            emit(None, None, r)
        else:
            emit(None, r, None)
    return rows


def render_csv(rows: list) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["REQ", "quadrant", "KYIV", "story", "SS", "task", "epic", "status"])
    w.writerows(rows)
    return buf.getvalue()


def render_report(s: Spec, res: dict) -> str:
    out = ["# Coverage report", "",
           "> GENERATED by `tools/trace.py`. Do not edit by hand. Reviewers read this file and its diff.", ""]

    def item(r, extra=""):
        k = s.effective_kyiv(r) if "type" in r else None
        title = f" {r['title'][:90]}" if r.get("title") else ""
        return f"- **{r['id']}**" + (f" [{k}]" if k else "") + f"{title}{extra} · `{r['file']}`"

    def section(title, lines):
        out.extend([f"### {title}", ""] + (lines or ["_none_"]) + [""])

    # summary
    out += ["## Summary", "", "| Artefact | Total | draft | in-review | approved | deprecated |", "|---|---|---|---|---|---|"]
    for label, group in (("Requirements", res["reqs"]), ("User/job stories", res["stories"]),
                         ("System stories", res["sss"]), ("Tasks", res["tasks"])):
        counts = [sum(r["status"] == st for r in group.values()) for st in ("draft", "in-review", "approved", "deprecated")]
        out.append(f"| {label} | {len(group)} | " + " | ".join(map(str, counts)) + " |")
    active_reqs = [r for r in res["reqs"].values() if r["status"] != "deprecated"]
    out += ["", "| Quadrant | " + " | ".join(QUADRANTS) + " |", "|---|---|---|---|---|",
            "| Requirements | " + " | ".join(str(sum(r["quadrant"] == q for r in active_reqs)) for q in QUADRANTS) + " |",
            "", "| KYIV | K | Y | I | V | none | provisional | final |", "|---|---|---|---|---|---|---|---|",
            "| Requirements | " + " | ".join(str(sum(r["kyiv"] == k for r in active_reqs)) for k in "KYIV")
            + f" | {sum(not r['kyiv'] for r in active_reqs)} | {sum(not r['kyiv_final'] for r in active_reqs)}"
            + f" | {sum(r['kyiv_final'] for r in active_reqs)} |", ""]
    empty_q = [q for q in QUADRANTS if active_reqs and not any(r["quadrant"] == q for r in active_reqs)]
    if empty_q:
        out += [f"**Red flag:** empty quadrant(s): {', '.join(empty_q)}.", ""]
    verdict = "OK, no K item has a coverage gap." if not res["k_gaps"] else f"**{len(res['k_gaps'])} K gap(s)**, trace.py exits 1."
    out += [f"**K coverage:** {verdict}", ""]
    out += [f"Sources registered: {', '.join(sorted(s.sources, key=natural)) or 'none'}.", ""]

    out += ["## Coverage gaps", ""]
    section("Requirements with no story (V excluded)", [item(r) for r in res["req_no_story"]])
    section("Stories with no system story", [item(r) for r in res["story_no_ss"]])
    section("System stories with no task", [item(r) for r in res["ss_no_task"]])
    section("Tasks with no requirement", [item(r) for r in res["task_no_req"]])
    section("Artefacts with no source (SRC or CTX)", [item(r) for r in res["no_source"]])
    section("Parked (V) requirements without stories (expected, for visibility)", [item(r) for r in res["parked_no_story"]])

    out += ["## Priority (KYIV)", ""]
    section("Missing KYIV", [item(r) for r in res["missing_kyiv"]])
    section("Priority conflicts: child ranked above all its parents",
            [item(r, f" is {r['kyiv']}, parents max {e}") for r, e in res["conflicts"]])
    section("Inheritance mismatch without kyiv_override_reason",
            [item(r, f" is {r['kyiv']}, inherits {e}") for r, e in res["mismatches"]])
    section("Overrides with a reason", [item(r, f" is {r['kyiv']}, inherits {e}: {r['override']}") for r, e in res["overrides"]])

    out += ["## Staleness", ""]
    section("Stale: approved, but a parent changed after approval",
            [item(r, f" approved against {p} v{old}, now v{new}") for r, p, old, new in res["stale"]])
    section("Approved without an approved_with stamp (staleness cannot be checked)",
            [item(r, f" missing: {', '.join(m)}") for r, m in res["unstamped"]])

    out += ["## Integrity", ""]
    section("Duplicate IDs", [f"- **{i}** in `{a}` and `{b}`" for i, a, b in s.duplicates])
    section("Dangling references", [f"- **{r['id']}** `{f}` → {v} (not defined) · `{r['file']}`" for r, f, v in res["dangling"]])
    section("Front-matter problems", [item(r, f": {msg}") for r, msg in res["fm_problems"]])
    section("Parse problems", [f"- `{f}`: {msg}" for f, msg in s.problems])
    section("Feature membership (each requirement in exactly one feature)", [item(r, f": {msg}") for r, msg in res["features"]])
    section("Task dependency cycles", [f"- {' → '.join(c)}" for c in res["cycles"]])
    section("depends_on / blocks not mirrored", [f"- {a} blocks {b}, but only one side says so" for a, b in res["block_mismatch"]])
    return "\n".join(out).rstrip() + "\n"


def sync_traces_to(text: str, traces: dict) -> str:
    """Rewrite each task's traces_to line in place, keeping layout and comments."""
    out, current, skip_indent = [], None, None
    for line in text.splitlines(keepends=True):
        if skip_indent is not None:
            if re.match(rf"^{skip_indent}\s+-\s", line):
                continue  # drop old block-style list items
            skip_indent = None
        m = re.match(r"^\s*-\s+id:\s*['\"]?(T-\d+)", line)
        if m:
            current = m.group(1)
        m = re.match(r"^(\s*)traces_to:[ \t]*(\[[^\]]*\])?[ \t]*(#.*)?$", line.rstrip("\n"))
        if m and current in traces:
            comment = f"  {m.group(3)}" if m.group(3) else ""
            out.append(f"{m.group(1)}traces_to: [{', '.join(traces[current])}]{comment}\n")
            if m.group(2) is None:
                skip_indent = m.group(1)
            continue
        out.append(line)
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--check", action="store_true", help="write nothing; fail if generated files are out of date")
    args = ap.parse_args()

    s = Spec(args.root.resolve())
    res = analyse(s)
    outputs = {
        s.spec / "90-trace" / "trace.csv": render_csv(trace_rows(s, res)),
        s.spec / "90-trace" / "coverage-report.md": render_report(s, res),
    }
    if s.tasks_text is not None:
        outputs[s.spec / "40-tasks" / "tasks.yaml"] = sync_traces_to(s.tasks_text, res["traces_to"])

    outdated = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if not args.check:
        for p in outdated:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(outputs[p], encoding="utf-8")

    print(f"REQ {len(res['reqs'])} · stories {len(res['stories'])} · SS {len(res['sss'])} · tasks {len(res['tasks'])}"
          f" · sources {len(s.sources)}")
    print(f"gaps: req→story {len(res['req_no_story'])}, story→SS {len(res['story_no_ss'])}, "
          f"SS→task {len(res['ss_no_task'])}, task→REQ {len(res['task_no_req'])}, no source {len(res['no_source'])}, "
          f"dangling {len(res['dangling'])}, stale {len(res['stale'])}")
    for p in outdated:
        print(("out of date: " if args.check else "updated: ") + s.rel(p))
    failed = bool(res["k_gaps"] or s.duplicates or s.problems or (args.check and outdated))
    if res["k_gaps"]:
        print(f"FAIL: {len(res['k_gaps'])} K item(s) with a coverage gap", file=sys.stderr)
    if s.duplicates or s.problems:
        print(f"FAIL: {len(s.duplicates)} duplicate id(s), {len(s.problems)} parse problem(s)", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
