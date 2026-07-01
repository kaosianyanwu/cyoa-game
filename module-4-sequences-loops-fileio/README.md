# Module 4 — Sequences, Loops, and File I/O

## What you're building

Refactor your story into a **list of scenes** and a **`while` loop** that keeps playing until the story ends. When the player reaches an ending, **write the result to a text file** (your first file I/O).

## Why it matters

Lists hold ordered data (your scene sequence). Loops let you repeat the "show scene → get choice → advance" pattern without copy-pasting code. Writing to a file persists something after the program exits.

## Acceptance criteria

- [ ] Story scenes are stored in a **list** (or list of structures you index into).
- [ ] A **`while` loop** drives the game until an ending is reached.
- [ ] At least **3 scenes** are playable (opening + branches toward an ending).
- [ ] On ending, writes something to a file (e.g. player name + ending title) using `open(..., "w")`.
- [ ] All tests in `test_module4.py` pass.

## Explain your code

Before you open your PR, write 2–3 sentences answering:

> How does your `while` loop know when to stop? What exactly gets written to the file, and where does the file appear when you run the program?

Paste your answer into the PR description.
