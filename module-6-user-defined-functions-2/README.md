# Module 6 — User-Defined Functions (Part 2)

## What you're building

Finish refactoring Module 5: move **all** scene/choice/ending logic into well-named functions so `main()` is a short, readable outline of the game flow.

## Why it matters

Clean function boundaries make bugs easier to find and set you up for adding stats (Module 7) and dictionary data (Module 8) without rewriting everything.

## Acceptance criteria

- [ ] `main()` is mostly function calls — no large blocks of inline logic.
- [ ] At least **four** functions besides `main()` (e.g. `show_scene`, `get_choice`, `play_turn`, `write_ending`, `run_game`).
- [ ] Choice labels are shown with meaningful text (not just `"..."` placeholders).
- [ ] Game plays through multiple scenes to an ending and writes the log file.
- [ ] All tests in `test_module6.py` pass.

## Explain your code

Before you open your PR, write 2–3 sentences answering:

> Which function would you change first if you wanted to add a third choice to every scene? Why did you split responsibilities the way you did?

Paste your answer into the PR description.
