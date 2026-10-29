---
id: CHANGELOG
type: changelog
title: Approved changes to the baseline
status: approved
owner: Mykola Marchuk
version: 5
kyiv: null
parents: [REQUIREMENTS]
sources: []
---
# Changelog

Changes to approved artefacts (playbook §7, constitution spec convention 14). Each CR records its trigger, the changed
ids (with their new version), the impacted ids and who approved it. The triage that proposed CR-001 – CR-008 is
summarised in the Step 3 work; the changed rows are in requirements.md. CR-009 comes from the Step 3.3 triage of
the system stories, decided at Gate 3 (2026-10-28).

| CR | Date | Trigger | Changed | Impact | Approved by |
|---|---|---|---|---|---|
| CR-001 | 2026-10-28 | decision: Gate 2 cancel-without-code; Step 3 red team | REQ-241 (v2) | US-212, JS-221, US-220, JS-309, US-107, JS-106, JS-117, JS-120, JS-020 | Mykola Marchuk |
| CR-002 | 2026-10-28 | contradiction REQ-009 vs REQ-055 (Step 3 stories) | REQ-009 (v2) | US-009, US-127, US-406 | Mykola Marchuk |
| CR-003 | 2026-10-28 | Step 3 red team: queue order | REQ-189 (v2) | US-124 | Mykola Marchuk |
| CR-004 | 2026-10-28 | contradiction REQ-169 vs REQ-167, REQ-168 | REQ-169 (v2) | JS-210 | Mykola Marchuk |
| CR-005 | 2026-10-28 | contradiction REQ-219 vs REQ-089 | REQ-219 (v2) | US-223, JS-226 | Mykola Marchuk |
| CR-006 | 2026-10-28 | Step 3 red team: audit of finance and site-staff views | REQ-263 (v2) | US-325 | Mykola Marchuk |
| CR-007 | 2026-10-28 | Step 3 red team: site full at the pre-arrival check | REQ-148 (v2) | JS-019 | Mykola Marchuk |
| CR-008 | 2026-10-28 | new requirement from a source (SRC-C2@00:24:04) | REQ-336 (new, Y), epics.md FT-02.1 | JS-020 | Mykola Marchuk |
| CR-009 | 2026-10-28 | contradiction REQ-231 vs REQ-009 v2 and REQ-012 (Step 3.3 system stories, Gate 3) | REQ-231 (v2) | JS-407, US-406; SS-003, SS-005, SS-006, SS-101, SS-421 | Mykola Marchuk |
| CR-010 | 2026-10-28 | Gate 4 task critique (P4.2) and cleanup: clarifications within the requirements | SS-001, SS-020, SS-021, SS-026, SS-208, SS-222 (v2); design.md (v2: §8 parameters, §9 Phase 0 decisions); open-questions.md (v5: Q-065 – Q-071) | spec/40-tasks/tasks.yaml (T-124, T-314, T-318, T-322, T-532, T-928, T-993 and the handler tasks T-208, T-355, T-558, T-559, T-1011) | Mykola Marchuk |
| CR-011 | 2026-10-29 | Step 5 KYIV proposal (P5.1): the provisional K was not closed under the task graph (49 Y tasks were prerequisites of K tasks) | requirements.md (v4: 52 rows Y → K, still provisional; row versions unchanged); open-questions.md (v6: Q-072) | 39 stories, 52 system stories and 93 tasks copy the inherited K (P2), no version change; T-710 set to Y by a human override (kyiv_override_reason); tasks.md (v2) | Mykola Marchuk |
| CR-012 | 2026-10-29 | Design revision after Steps 3 and 4 (playbook §10.1): data-model.md and integrations.md were still v0 | data-model.md (v1: entities, relationships, lifecycles and invariants from the system stories and tasks; gaps G-1 – G-6); integrations.md (v1: MVP use, platform services I-20 – I-30, U-15 – U-24); design.md (v3: §2.4, §2.5); open-questions.md (v7: Q-073, Q-074; Q-047 now cites REQ-248) | T-122 builds the states of data-model.md §3; gaps G-1 – G-3 affect K work and need a CR on SS-040, T-180, T-1007 and the booking lifecycle | Mykola Marchuk |
