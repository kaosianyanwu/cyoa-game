# 🎮 cyoa-game

> **You write the story. Python runs it.** One module at a time, you'll build a choose-your-own-adventure game from scratch — ending with save/load and everything.

**New here?** [SETUP.md](SETUP.md) · **Checklist:** [TASKS.md](TASKS.md) · **Submit work:** [SUBMITTING_A_PR.md](SUBMITTING_A_PR.md)

Repo: [github.com/kaosianyanwu/cyoa-game](https://github.com/kaosianyanwu/cyoa-game)

Work at your own pace — no fixed weekly deadline. When you finish a module, open a PR ([SUBMITTING_A_PR.md](SUBMITTING_A_PR.md)). Kaosi schedules checkpoints as needed.

> 📖 **Optional peek:** `reference/` has a finished *Mall Run* example — inspiration only, not for copying.

---

## 🌿 Git basics

Same routine every module. Skim once, keep handy.

### Create a branch

Never commit straight to `main`. One branch per module:

```bash
git checkout -b module-1-yourname
```

Clear names help (`module-3-jamie`) — Kaosi can see where you are at a glance.

### Commit your work

Tests passing? Commit:

```bash
git status
git add module-1-introduction/game.py
git commit -m "Module 1: add title and name prompt"
```

One short line — what you did and why.

### Push & open a PR

```bash
git push -u origin module-1-yourname
```

Open a **Pull Request** into `main`, paste your “Explain your code” note. Full walkthrough: [SUBMITTING_A_PR.md](SUBMITTING_A_PR.md).

---

## 🔄 Module workflow

For each module ([TASKS.md](TASKS.md) has the checklist):

1. 📂 Read that module's `README.md`
2. ⌨️ Code until tests pass (`python3 -m pytest module-N-.../`)
3. ✍️ Write your “Explain your code” note in that README
4. 💬 Message Kaosi: **“Module N done, ready for a PR.”**
5. 🚀 Open the PR → review → merge ([SUBMITTING_A_PR.md](SUBMITTING_A_PR.md))
6. ➡️ Next module

After a merge, sync before branching again:

```bash
git checkout main
git pull
git checkout -b module-N-yourname
```

> **Carrying code forward:** Each module folder has its own `game.py`, but your *real* game grows in one place. After Module N merges, **copy your finished `game.py` into the next module's folder** before you start — then add that module's new concept on top. Don't start from scratch unless Kaosi says to.

Plan your story in `GAME_PLAN.md`. Don't copy `reference/`.

---

## 🗺️ Module roadmap

| Module | Folder | Concept |
|:------:|--------|---------|
| 🏁 **1** | `module-1-introduction/` | `print`, `input`, strings |
| 📝 **2** | `module-2-simple-statements/` | Variables, hardcoded scene |
| 🔀 **3** | `module-3-conditional-statements/` | `if` / `elif` / `else` |
| 🔁 **4** | `module-4-sequences-loops-fileio/` | Lists, `while`, file I/O |
| 🧩 **5** | `module-5-user-defined-functions-1/` | First functions |
| ✂️ **6** | `module-6-user-defined-functions-2/` | Refactor with functions |
| 📊 **7** | `module-7-multidimensional-lists/` | Tracked stat (e.g. budget)¹ |
| 🗃️ **8** | `module-8-dictionaries/` | Story as `dict` data |
| 💾 **9** | `module-9-classes/` | `Player` class, JSON save/load |

---

## 🤖 AI use policy

| Modules | Rule |
|---------|------|
| **1–6** | 🚫 No pasting errors or code into AI for fixes. Notes + Kaosi. |
| **7–9** | ✅ AI okay for debugging — understand every line you ship. |

When in doubt, ask Kaosi first.

¹ Module 7 folder name matches the syllabus unit; the task is adding a tracked stat that changes with choices.
