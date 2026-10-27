#!/usr/bin/env python3
"""Extract plain text from spec/00-inputs/* into spec/00-inputs/_extracted/.

Each input must be named <ID>_<name>.<ext> (e.g. D1_Client_Deck_Sep2026.pptx) and becomes SRC-<ID>.
Extracts keep the anchors used in citations:
  .pptx  ->  "## SRC-D1#<slide>"  (slide text, then speaker notes)
  .docx  ->  "[hh:mm:ss] Speaker (Company): text"  ->  cite as SRC-C1@hh:mm:ss
  .html  ->  "## SRC-R1#<element id>" for every heading or list item with an id

Also writes _extracted/_index.md, the source register (IDs, files, sha256, anchors).
Stdlib only. Usage: python3 tools/extract.py
"""
import hashlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUTS = ROOT / "spec" / "00-inputs"
OUT = INPUTS / "_extracted"

# Who wrote each source. Matters for the Requirements Quadrant: only the client "states".
ORIGIN = {
    "D1": ("client deck", "Amperlane (client)"),
    "C1": ("call transcript", "Amperlane + Intellias (speaker per line)"),
    "C2": ("call transcript", "Amperlane + Intellias (speaker per line)"),
    "D2": ("vendor deck", "Intellias (vendor), sent to client"),
    "R1": ("internal recap", "Intellias presales (internal wiki page)"),
}

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PKG_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
DC = "{http://purl.org/dc/elements/1.1/}"


def core_props(z: zipfile.ZipFile) -> dict:
    if "docProps/core.xml" not in z.namelist():
        return {}
    root = ET.fromstring(z.read("docProps/core.xml"))
    return {k: (root.findtext(DC + k) or "").strip() for k in ("title", "subject", "creator")}


def rels(z: zipfile.ZipFile, part: str) -> dict:
    """Map rId -> target path for an OPC part."""
    folder, name = part.rsplit("/", 1)
    rel_path = f"{folder}/_rels/{name}.rels"
    if rel_path not in z.namelist():
        return {}
    out = {}
    for r in ET.fromstring(z.read(rel_path)).iter(PKG_REL + "Relationship"):
        target = r.get("Target")
        parts = (folder + "/" + target).split("/") if not target.startswith("/") else target[1:].split("/")
        norm = []
        for p in parts:
            if p == "..":
                norm.pop()
            elif p not in ("", "."):
                norm.append(p)
        out[r.get("Id")] = "/".join(norm)
    return out


# ---------- pptx ----------

def para_text(p: ET.Element) -> str:
    chunks = []
    for el in p.iter():
        if el.tag == A + "t":
            chunks.append(el.text or "")
        elif el.tag == A + "br":
            chunks.append("\n")
    return "".join(chunks).strip()


def shape_paras(sp: ET.Element) -> list:
    return [t for t in (para_text(p) for p in sp.iter(A + "p")) if t]


def placeholder_type(sp: ET.Element) -> str:
    ph = sp.find(f"{P}nvSpPr/{P}nvPr/{P}ph")
    return "" if ph is None else (ph.get("type") or "body")


def slide_blocks(root: ET.Element) -> tuple:
    """Return (title, [block text]) in document order; tables become pipe rows."""
    title, blocks = "", []
    for el in root.iter():
        if el.tag == P + "sp":
            paras = shape_paras(el)
            if not paras:
                continue
            if placeholder_type(el) in ("title", "ctrTitle") and not title:
                title = " ".join(paras)
            blocks.append("\n".join(paras))
        elif el.tag == A + "tbl":
            rows = []
            for tr in el.iter(A + "tr"):
                cells = [" ".join(shape_paras(tc)).replace("|", "\\|") for tc in tr.iter(A + "tc")]
                rows.append("| " + " | ".join(cells) + " |")
            blocks.append("\n".join(rows))
    return title, blocks


def extract_pptx(path: Path, src: str) -> tuple:
    z = zipfile.ZipFile(path)
    pres_rels = rels(z, "ppt/presentation.xml")
    pres = ET.fromstring(z.read("ppt/presentation.xml"))
    slide_parts = [pres_rels[s.get(R + "id")] for s in pres.iter(P + "sldId")]
    lines, anchors = [], []
    for n, part in enumerate(slide_parts, start=1):
        title, blocks = slide_blocks(ET.fromstring(z.read(part)))
        anchors.append(f"#{n}")
        lines.append(f"## SRC-{src}#{n}" + (f" — {title}" if title else ""))
        lines.append("")
        lines.append("\n\n".join(blocks) if blocks else "_(no text on slide)_")
        notes_part = next((t for t in rels(z, part).values() if "notesSlide" in t), None)
        if notes_part:
            notes_root = ET.fromstring(z.read(notes_part))
            notes = [
                "\n".join(shape_paras(sp))
                for sp in notes_root.iter(P + "sp")
                if placeholder_type(sp) not in ("sldNum", "sldImg", "hdr", "ftr", "dt") and shape_paras(sp)
            ]
            if notes:
                lines.append("")
                lines.append("**Speaker notes:**")
                lines.append("")
                lines.append("\n\n".join(notes))
        lines.append("")
    meta = core_props(z)
    stats = f"{len(slide_parts)} slides"
    return meta, lines, stats, f"SRC-{src}#1 … SRC-{src}#{len(slide_parts)}"


# ---------- docx ----------

SPEAKER = re.compile(r"^(?P<name>.+?)\s+\((?P<org>.+?)\)\s+(?P<ts>\d\d:\d\d:\d\d)$")


def w_text(el: ET.Element) -> str:
    chunks = []
    for x in el.iter():
        if x.tag == W + "t":
            chunks.append(x.text or "")
        elif x.tag in (W + "tab",):
            chunks.append("\t")
        elif x.tag in (W + "br", W + "cr"):
            chunks.append("\n")
    return "".join(chunks).strip()


def extract_docx(path: Path, src: str) -> tuple:
    z = zipfile.ZipFile(path)
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    lines, turns, first_ts, last_ts = [], 0, None, None
    pending = None  # speaker header waiting for its utterance
    for el in body:
        if el.tag == W + "tbl":
            rows = [[w_text(tc).replace("|", "\\|") for tc in tr.iter(W + "tc")] for tr in el.iter(W + "tr")]
            for i, row in enumerate(rows):
                lines.append("| " + " | ".join(row) + " |")
                if i == 0 and len(rows) > 1 and row[0] in ("Name",):
                    lines.append("|" + "---|" * len(row))
            lines.append("")
            continue
        if el.tag != W + "p":
            continue
        text = w_text(el)
        if not text:
            continue
        m = SPEAKER.match(text)
        if m:
            if pending:  # header with no utterance: keep it visible
                lines.append(f"[{pending['ts']}] {pending['name']} ({pending['org']}):")
            pending = m.groupdict()
            continue
        if pending:
            lines.append(f"[{pending['ts']}] {pending['name']} ({pending['org']}): {text}")
            first_ts = first_ts or pending["ts"]
            last_ts = pending["ts"]
            turns += 1
            pending = None
        else:
            lines.append(f"## {text}" if text in ("Attendees", "Transcript") else text)
            lines.append("")
    if pending:
        lines.append(f"[{pending['ts']}] {pending['name']} ({pending['org']}):")
    # Comments, footnotes and endnotes would carry evidence too; surface them if present.
    for part, label in (("word/comments.xml", "Comments"), ("word/footnotes.xml", "Footnotes"), ("word/endnotes.xml", "Endnotes")):
        if part in z.namelist():
            items = [w_text(p) for p in ET.fromstring(z.read(part)).iter(W + "p")]
            items = [t for t in items if t]
            if items:
                lines += ["", f"## {label}", ""] + items
    meta = core_props(z)
    stats = f"{turns} speaker turns, {first_ts}–{last_ts}"
    return meta, lines, stats, f"SRC-{src}@{first_ts} … SRC-{src}@{last_ts}"


# ---------- html ----------

class HtmlToText(HTMLParser):
    """Small HTML -> Markdown-ish converter: headings, paragraphs, lists, tables, links."""

    BLOCK = {"p", "div", "section", "main", "nav", "details", "summary", "ul", "ol", "table", "tr", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "li"}
    INLINE_SOFT = {"span", "b", "strong", "i", "em", "small", "sup", "a", "code"}
    SKIP = {"style", "script", "head", "title"}
    SKIP_CLASSES = {"act", "caret"}  # UI chrome: "Reply · Like", tree carets

    def __init__(self, src: str):
        super().__init__(convert_charrefs=True)
        self.src = src
        self.out, self.buf = [], []
        self.skip_tag, self.skip_depth = None, 0
        self.lists = []  # stack of [kind, counter]
        self.row, self.cell, self.in_table = None, None, 0
        self.href = None
        self.anchors = []
        self.title = ""
        self._in_h1 = False
        self.comments = 0
        self.prefix = ""  # anchor label for the next flushed line

    def flush(self):
        text = "".join(self.buf)
        text = re.sub(r"(?<=[\w\]\)%.:;!?])\x00+(?=[\w\[(@])", " ", text).replace("\x00", "")
        indent = re.match(r" *", text).group(0)
        text = re.sub(r"[ \t\r\n]+", " ", text).strip()
        self.buf = []
        if not text or re.fullmatch(r"-|\d+\.", text):  # skip empty list items
            return
        self.out.append(indent + self.prefix + text)
        self.prefix = ""
        if not self.lists:
            self.out.append("")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip_tag:
            self.skip_depth += tag == self.skip_tag
            return
        classes = set((a.get("class") or "").split())
        if tag in self.SKIP or a.get("aria-hidden") == "true" or classes & self.SKIP_CLASSES:
            self.skip_tag, self.skip_depth = tag, 1
            return
        if tag == "section" and "comments" in classes:
            self.flush()
            self.anchors.append("#comments")
            self.out += ["", f"## SRC-{self.src}#comments — Comments", ""]
        elif tag == "div" and "c" in classes:
            self.flush()
            self.comments += 1
            self.anchors.append(f"#c{self.comments}")
            self.prefix = f"[SRC-{self.src}#c{self.comments}] "
            return
        elif tag == "span" and "when" in classes:
            self.buf.append(" · ")
        if self.in_table and tag in ("td", "th"):
            self.cell = []
            return
        if tag == "table":
            self.flush()
            self.in_table += 1
            self.rows, self.header_done = [], False
            return
        if tag == "tr" and self.in_table:
            self.row = []
            return
        if tag in self.BLOCK:
            self.flush()
        if tag in ("ul", "ol"):
            self.lists.append([tag, 0])
        elif tag == "li":
            prefix = "  " * (len(self.lists) - 1)
            if self.lists and self.lists[-1][0] == "ol":
                self.lists[-1][1] += 1
                prefix += f"{self.lists[-1][1]}. "
            else:
                prefix += "- "
            if a.get("id"):
                self.anchors.append("#" + a["id"])
                prefix += f"[SRC-{self.src}#{a['id']}] "
            self.buf.append(prefix)
        elif re.fullmatch(r"h[1-6]", tag):
            level = int(tag[1])
            self.out.append("")
            if a.get("id"):
                self.anchors.append("#" + a["id"])
                self.buf.append("#" * level + f" SRC-{self.src}#{a['id']} — ")
            else:
                self.buf.append("#" * level + " ")
            self._in_h1 = tag == "h1"
        elif tag == "hr":
            self.out.append("* * *")
        elif tag == "summary":
            self.buf.append("▸ ")
        elif tag == "a":
            self.href = a.get("href") or ""
            self._target = self.cell if self.cell is not None else self.buf
            self._target.append("\x00")
        elif tag == "span" and any(c in (a.get("class") or "").split() for c in ("lz", "label", "jira")):
            (self.cell if self.cell is not None else self.buf).append("\x00[")
        elif tag in self.INLINE_SOFT:
            (self.cell if self.cell is not None else self.buf).append("\x00")
        elif tag == "br":
            (self.cell if self.cell is not None else self.buf).append(" ")

    def handle_endtag(self, tag):
        if self.skip_tag:
            if tag == self.skip_tag:
                self.skip_depth -= 1
                if not self.skip_depth:
                    self.skip_tag = None
            return
        if self.in_table and tag in ("td", "th"):
            text = "".join(self.cell)
            text = re.sub(r"(?<=[\w\]\)%.:;!?])\x00+(?=[\w\[(@])", " ", text).replace("\x00", "")
            self.row.append(re.sub(r"\s+", " ", text).strip().replace("|", "\\|"))
            self.cell = None
            return
        if tag == "tr" and self.in_table:
            self.rows.append(self.row)
            self.row = None
            return
        if tag == "table":
            self.in_table -= 1
            for i, row in enumerate(self.rows):
                self.out.append("| " + " | ".join(row) + " |")
                if i == 0:
                    self.out.append("|" + "---|" * len(row))
            self.out.append("")
            return
        if tag == "a":
            target = self._target
            if self.href.startswith("http"):
                target.append(f" <{self.href}>")
            target.append("\x00")
            self.href = None
            return
        if tag == "span":
            target = self.cell if self.cell is not None else self.buf
            # close a "[label" opened above
            joined = "".join(target)
            if joined.count("\x00[") > joined.count("]\x00"):
                target.append("]\x00")
            else:
                target.append("\x00")
            return
        if tag in self.INLINE_SOFT:
            (self.cell if self.cell is not None else self.buf).append("\x00")
            return
        if tag in ("ul", "ol") and self.lists:
            self.flush()
            self.lists.pop()
            if not self.lists:
                self.out.append("")
            return
        if tag in self.BLOCK:
            if self._in_h1 and tag == "h1":
                self.title = re.sub(r"^#+\s*", "", re.sub(r"\s+", " ", "".join(self.buf))).strip()
                self._in_h1 = False
            self.flush()
            if re.fullmatch(r"h[1-6]|p|summary", tag):
                self.out.append("")

    def handle_data(self, data):
        if self.skip_tag:
            return
        (self.cell if self.cell is not None else self.buf).append(data)


def extract_html(path: Path, src: str) -> tuple:
    html = path.read_text(encoding="utf-8")
    parser = HtmlToText(src)
    parser.feed(html)
    parser.flush()
    lines = []
    for line in parser.out:  # collapse runs of blank lines
        if line == "" and lines and lines[-1] == "":
            continue
        lines.append(line)
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    meta = {"title": parser.title or (title.group(1).strip() if title else ""), "subject": "", "creator": ""}
    stats = f"{len(parser.anchors)} anchors"
    return meta, lines, stats, ", ".join(f"SRC-{src}{a}" for a in parser.anchors)


# ---------- main ----------

EXTRACTORS = {".pptx": extract_pptx, ".docx": extract_docx, ".html": extract_html, ".htm": extract_html}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    order = list(ORIGIN)  # chronological, as registered above; unknown sources last
    files = sorted(
        (p for p in INPUTS.iterdir() if p.is_file() and not p.name.startswith(".")),
        key=lambda p: (order.index(p.name.split("_")[0]) if p.name.split("_")[0] in order else len(order), p.name),
    )
    for path in files:
        m = re.match(r"^([A-Z]+\d+)_", path.name)
        if not m:
            print(f"skip (no <ID>_ prefix): {path.name}", file=sys.stderr)
            continue
        src = m.group(1)
        fn = EXTRACTORS.get(path.suffix.lower())
        if not fn:
            print(f"skip (no extractor for {path.suffix}): {path.name}", file=sys.stderr)
            continue
        meta, body, stats, anchors = fn(path, src)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        kind, origin = ORIGIN.get(src, ("unknown", "unknown: set ORIGIN in tools/extract.py"))
        title = meta.get("title") or path.stem
        front = [
            "---",
            f"id: SRC-{src}",
            "type: source",
            f"title: {title!r}" if ":" in title else f"title: {title}",
            f"kind: {kind}",
            f"origin: {origin!r}" if ":" in origin else f"origin: {origin}",
            f"original: {path.name}",
            f"sha256: {sha}",
            "generated_by: tools/extract.py  # do not edit; regenerate instead",
            "---",
            "",
            f"# SRC-{src} · {title}",
            "",
        ]
        if meta.get("subject"):
            front += [f"_{meta['subject']}_" + (f" · author: {meta['creator']}" if meta.get("creator") else ""), ""]
        out = OUT / (path.stem + ".md")
        out.write_text("\n".join(front + body).rstrip() + "\n", encoding="utf-8")
        index.append((src, path.name, out.name, kind, origin, title, stats, anchors, sha))
        print(f"SRC-{src}: {path.name} -> {out.relative_to(ROOT)} ({stats})")

    lines = [
        "---",
        "type: source-index",
        "generated_by: tools/extract.py  # do not edit; regenerate instead",
        "---",
        "",
        "# Source register",
        "",
        "Cite as `SRC-<id>#<slide>` (decks), `SRC-<id>@<hh:mm:ss>` (transcripts), `SRC-<id>#<anchor>` (HTML).",
        "Speaker notes belong to their slide: cite the slide number.",
        "",
        "| SRC | Kind | Origin | Title | Original | Extract | Coverage | Anchors |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for src, orig, ext, kind, origin, title, stats, anchors, _ in index:
        lines.append(f"| SRC-{src} | {kind} | {origin} | {title} | `{orig}` | [{ext}]({ext}) | {stats} | {anchors} |")
    lines += ["", "## Integrity (sha256 of originals)", ""]
    lines += [f"- `{orig}` `{sha}`" for _, orig, *_rest, sha in index]
    (OUT / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
