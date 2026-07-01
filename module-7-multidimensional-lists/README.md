# 📊 Module 7 — Multi-Dimensional Lists

> **Start here:** copy your finished Module 6 `game.py` into this folder first.

## What you're building

A **tracked stat** (budget, energy, courage — your pick). At least one choice changes it.

## Why it matters

This module matches your syllabus unit on **multi-dimensional lists** — structured data nested inside other structures.

You already have that pattern: `SCENES` is a **list**, and each scene is a **dict** inside it. Module 7 adds **game state** the same way — values that persist and update across turns (e.g. `stats = {"budget": 60}`). Choices read and modify that structured data, like inventory rows `[["potion", 3], ["gold", 60]]` would in a bigger game.

State that changes turn to turn — health, money, score — is how CYOA games stay interesting.

> 🤖 **AI tools allowed from this module on** — see [README AI policy](../README.md#-ai-use-policy). Still explain every line you submit.

## Acceptance criteria

- [ ] Tracked stat added
- [ ] At least one choice modifies it
- [ ] `python3 -m pytest module-7-multidimensional-lists/`

## Explain your code

2–3 sentences here:

> Which choices change the stat? Same ending, different stat values possible?

Then message Kaosi: **"Module 7 done, ready for a PR."** → [SUBMITTING_A_PR.md](../SUBMITTING_A_PR.md)

---

*Your answer goes above ↑ and in the PR description.*
