# cyoa-game

**New here? Start with [SETUP.md](SETUP.md) before anything else.**

Build your own choose-your-own-adventure (CYOA) game in Python, one module at a time. Each module adds one new language concept to the same project until you have a playable story with save/load. Work through modules at your own pace — when you finish one, open a PR; checkpoints with Kaosi are scheduled as needed, not on a fixed weekly cycle.

Optional read (not required): `reference/` has a finished Mall Run example (`game.py` + `EXAMPLE_GAME_PLAN.md`) showing what the end state looks like — use it for inspiration, not as something to copy.

## Git basics

You will use the same Git workflow for every module. Read through this once and keep it open while you work.

### Create a branch for your work

Never commit directly to `main`. Make a new branch for each module:

```bash
git checkout -b module-1-yourname
```

Use a clear branch name like `module-3-jamie` so Kaosi can tell which module you are on.

### Commit your changes

After you finish coding and tests pass:

```bash
git status
git add module-1-introduction/game.py
git commit -m "Module 1: add title and name prompt"
```

Write commit messages in plain English — say *what* you did and *why* in one short line.

### Push and open a pull request (PR)

```bash
git push -u origin module-1-yourname
```

On GitHub, open a **Pull Request** from your branch into `main`. In the PR description, paste your “Explain your code” write-up from the module README.

Kaosi will review the PR, leave comments, and merge when it is ready.

## Module workflow

There is no fixed weekly deadline. Complete modules in order, at a pace that works for you. When you finish a module, open a PR — Kaosi will review it and schedule the next checkpoint as needed.

Repeat these steps for each module:

1. **Pull latest `main`** (after Kaosi merges your previous PR):
   ```bash
   git checkout main
   git pull
   git checkout -b module-N-yourname
   ```
2. **Open the module folder** (e.g. `module-2-simple-statements/`).
3. **Read `README.md`** in that folder — it is your ticket for that module.
4. **Plan your story** in the top-level `GAME_PLAN.md` before you code (premise, scenes, endings). Do not copy the example game; invent your own theme.
5. **Edit `game.py`** — replace `# TODO` markers and fill in your story from your game plan.
6. **Make tests pass:**
   ```bash
   python3 -m pytest module-N-.../test_moduleN.py -v
   ```
7. **Write your “Explain your code”** answer (2–3 sentences) in the module README or PR description.
8. **Open a PR** for Kaosi to review.

Each module’s `game.py` builds on the *finished* code from the previous module. After your PR is merged, use that working code as the starting point for the next module (or pull from `main` if the repo is updated that way).

## Module roadmap

| Module | Folder | Concept |
|--------|--------|---------|
| 1 | `module-1-introduction/` | `print`, `input`, strings |
| 2 | `module-2-simple-statements/` | Variables, hardcoded scene |
| 3 | `module-3-conditional-statements/` | `if` / `elif` / `else` |
| 4 | `module-4-sequences-loops-fileio/` | Lists, `while`, file write |
| 5 | `module-5-user-defined-functions-1/` | First functions |
| 6 | `module-6-user-defined-functions-2/` | Refactor with functions |
| 7 | `module-7-multidimensional-lists/` | Tracked stat (e.g. budget) |
| 8 | `module-8-dictionaries/` | Story as `dict` data |
| 9 | `module-9-classes/` | `Player` class, JSON save/load |

## AI use policy

- **Modules 1–6:** Do **not** paste error messages, stack traces, or your code into AI tools to get fixes. Use your notes and ask Kaosi. Struggling with syntax is part of learning.
- **Modules 7–9:** You **may** use AI as a debugging assistant (explain errors, suggest fixes). You must still understand and be able to explain every line you submit.

When in doubt, ask Kaosi before using AI.
