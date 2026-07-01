# Module 8 — Dictionaries

## What you're building

Convert your story from a **list indexed by number** to a **`STORY` dictionary**: each scene is keyed by an id string (e.g. `"start"`) with `text`, `choices`, and optional `ending` / `stat_effect`.

## Why it matters

Dictionaries map names to data — perfect for scene ids like `"forest"` or `"ending_a"`. This is how professional CYOA engines store story content separately from game logic (see the reference example for the target shape).

## Acceptance criteria

- [ ] Defines **`STORY`** as a `dict` keyed by scene id strings.
- [ ] Each scene has at least `"text"`; branching scenes have `"choices"` mapping option → `(label, next_scene_id)`.
- [ ] Ending scenes use an `"ending"` key instead of choices.
- [ ] Game loop looks up scenes by id (`STORY[scene_id]`) instead of list index.
- [ ] Stat tracking from Module 7 still works.
- [ ] All tests in `test_module8.py` pass.

## Explain your code

Before you open your PR, write 2–3 sentences answering:

> Why is `"start"` a better scene key than `0`? How would you add a new scene without renumbering other scenes?

Paste your answer into the PR description.
