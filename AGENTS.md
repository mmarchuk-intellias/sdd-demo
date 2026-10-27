# AGENTS.md — spec repository

You are working in a spec-driven repository. The spec is the source of truth.

## Always
- Read spec/constitution.md and this file before any task.
- Work only on the step you were asked to do. Never skip a human review gate.
- Every artefact you create has YAML front-matter: id, type, title, status, owner, sources, parents, kyiv, version.
- New artefacts start with status: draft. Never set status: approved; only humans do that.
- Every claim about the client, users, numbers or constraints cites a source:
  SRC-<doc>[@<timestamp>|#<slide>].
- When sources conflict, do not pick one silently. Add an entry to spec/01-context/conflicts.md
  and apply the resolution rule: later > earlier, specific > general, data > estimate.
  Mark the conflict "needs-decision" if the rule doesn't settle it.
- When something is unknown, write an assumption (A-###) or an open question (Q-###)
  in spec/01-context/open-questions.md. Never invent facts to fill gaps.
- After any change, run `python tools/trace.py` and include the coverage-report diff in your summary.

## Never
- Edit anything in spec/00-inputs/.
- Delete an approved artefact. Deprecate it instead (status: deprecated, superseded_by: <id>).
- Reuse or renumber an ID.
- Put implementation code in spec files. Snippets are allowed only in design.md and ADRs.

## Formats
- User stories: "As a <role>, I want <capability>, so that <benefit>." AC in Gherkin.
- Job stories: "When <situation>, I want to <motivation>, so I can <outcome>." AC in Gherkin.
- System stories: "As the <system/component>, I need <capability>, so that <outcome>."
  AC in EARS only (Ubiquitous / When / While / If-then / Where).
- Requirements: one sentence, testable, quadrant-tagged (S-F, S-NF, U-F, U-NF).
- Priorities: KYIV (K / Y / I / V), see constitution.md.

## When finished
Summarise what you created or changed (IDs), open conflicts, new questions and coverage gaps.
Then stop and wait for human review.

---

# Project specifics: Amperlane presale

The rules above are generic. This part adds what is specific to this repository.

## Sources

Read the plain-text extracts in `spec/00-inputs/_extracted/`, not the binaries. The register with hashes is
`spec/00-inputs/_extracted/_index.md`.

| SRC | What | Origin | Cite as |
|---|---|---|---|
| SRC-D1 | Amperlane "Platform Partner Brief" deck, Sep 2026 | client | `SRC-D1#<slide>` |
| SRC-C1 | Call 1 · Discovery transcript, 2026-09-29 | client + Intellias | `SRC-C1@<hh:mm:ss>` |
| SRC-C2 | Call 2 · Technical deep-dive transcript, 2026-10-08 | client + Intellias | `SRC-C2@<hh:mm:ss>` |
| SRC-D2 | Intellias "Our understanding & solution direction" deck, 2026-10-16 | vendor | `SRC-D2#<slide>` |
| SRC-R1 | Intellias internal account brief (wiki page), last updated 2026-10-19 | vendor, internal | `SRC-R1#<anchor>` (e.g. `#pilot`, `#r5`, `#c1`) |

- Speaker notes belong to their slide: cite the slide number.
- Transcripts: cite the timestamp of the line that carries the claim.
- **Who said it matters.** "Stated" (S-F, S-NF) means said or written by the client: SRC-D1, and Amperlane speakers in
  SRC-C1/C2. SRC-D2 and SRC-R1 are Intellias' interpretation. Use them as evidence, but a requirement that only they
  support is not "stated" by the client.
- `CASE_BIBLE.md` is the case author's reference, not a presale input.
  It is deliberately not in this repository. Do not look for it or use it as a source.

## Tools

- `python3 tools/extract.py` regenerates `_extracted/` (stdlib only). Run it only when a new input lands in
  `spec/00-inputs/`; new inputs are named `<ID>_<name>.<ext>`, and their origin is registered in
  `ORIGIN` inside the script. Never edit extracts by hand.
- `python tools/trace.py` above means `uv run tools/trace.py` (uv installs PyYAML on the fly),
  or `python3 tools/trace.py` with PyYAML installed. `--check` writes nothing and fails when outputs are stale.
  It exits 1 when a K item has a coverage gap.

## Machine-readable formats (parsed by tools/trace.py)

- **Requirements** (`spec/20-requirements/requirements.md`): one table row per requirement, columns in this order:
  `| REQ-### | S-F/S-NF/U-F/U-NF | sentence | SRC-…, CTX-… | K (provisional) | Q-/A- links | v1 | status |`.
  The last two columns are optional (default: v1, the file's status). Bump `vN` when a requirement's meaning changes.
  Rows under a heading containing "Parking lot" are parked. Other tables in this file must not start with a REQ id
  followed by a quadrant tag.
- **Epics** (`spec/30-stories/epics.md`): `| EP-## | title | grouping logic |` rows and
  `| FT-##.# | title | REQ-###, REQ-### |` rows. The REQ ids in an FT row are its members.
- **Context ids** (CTX, Q, A, CF) are defined where they start a line or table row in `spec/01-context/`.
- **Stories** link up via `requirements: [REQ-###]`. **System stories** via `parents: [US-/JS-###]` (or `[]` for
  enablers) plus `requirements: [REQ-###]`. **Tasks** via `implements: [SS-###]`; `traces_to` is filled by trace.py.
- **Approval stamp.** When a human approves a story, system story or task, add
  `approved_with: {<parent id>: <parent version>, ...}` for each parent. trace.py uses it to flag stale artefacts.
- `kyiv:` values are quoted or bare letters K, Y, I, V; overrides need `kyiv_override_reason:`.
