# Module 9 — Classes

## What you're building

Wrap player state in a **`Player` class** (name, current scene, stats) and add **JSON save/load** so a player can quit mid-story and resume later.

## Why it matters

Classes group related data and behavior. Serializing a `Player` to JSON is a real-world pattern for game saves, user profiles, and app state.

## Acceptance criteria

- [ ] Defines a **`Player`** class with `name`, `current_scene`, and `stats`.
- [ ] **`to_dict()`** and **`from_dict()`** (classmethod) convert Player ↔ JSON-friendly dict.
- [ ] **`save_game(player)`** writes JSON to a file after each choice (or at key moments).
- [ ] **`load_game()`** returns a `Player` if a save exists, else `None`.
- [ ] **`main()`** offers to resume when a save file is found.
- [ ] Full play-through still works; save file is removed or cleared on reaching an ending.
- [ ] All tests in `test_module9.py` pass.

## Explain your code

Before you open your PR, write 2–3 sentences answering:

> What data gets saved in JSON, and why is a class easier to save than three separate global variables?

Paste your answer into the PR description.
