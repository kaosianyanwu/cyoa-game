# Module 5 — User-Defined Functions (Part 1)

## What you're building

Extract **`show_scene()`** and **`get_choice()`** functions from your Module 4 loop so scene display and input validation live in reusable blocks.

## Why it matters

Functions reduce duplication and make your game easier to extend. You'll call the same helpers every time the loop shows a scene or reads a choice.

## Acceptance criteria

- [ ] Defines a **`show_scene(scene)`** function that prints scene text and choice labels.
- [ ] Defines a **`get_choice(valid_options)`** function that loops until input is valid.
- [ ] **`main()`** uses these functions inside the existing `while` loop.
- [ ] Game still plays through to an ending and writes the log file.
- [ ] All tests in `test_module5.py` pass.

## Explain your code

Before you open your PR, write 2–3 sentences answering:

> What does each function return (if anything)? Why is it better to validate input inside `get_choice()` instead of in `main()`?

Paste your answer into the PR description.
