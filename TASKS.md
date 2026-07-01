# ✅ Tasks

Nine modules, one story, in order. Each builds on the last — no skipping ahead. 😄

**Every module:**
1. 📂 Read that folder's `README.md`
2. ⌨️ Code until tests pass
3. ✍️ "Explain your code" note in that README
4. 💬 Message Kaosi: "Module N done, ready for a PR." ([SUBMITTING_A_PR.md](SUBMITTING_A_PR.md))
5. 🚀 Open PR → review → merge ([SUBMITTING_A_PR.md](SUBMITTING_A_PR.md))
6. ➡️ Next module

> **After each merge:** copy your finished `game.py` into the **next** module's folder before you start. One growing game, nine new concepts.

No fixed weekly deadline — checkpoints with Kaosi as needed.

---

## Module 0 — Setup 🛠️
- [ ] Python, Git, GitHub auth ([SETUP.md](SETUP.md))
- [ ] Repo cloned
- [ ] `python3 -m pytest module-1-introduction/test_module1.py -v` runs (failing OK)
- [ ] [GAME_PLAN.md](GAME_PLAN.md) filled out

## Module 1 — Introduction 🏁
- [ ] Game prints a title
- [ ] Asks name with `input()`
- [ ] Greets player by name
- [ ] `python3 -m pytest module-1-introduction/`

## Module 2 — Simple Statements 📝
- [ ] Scene text in a variable, printed
- [ ] Hardcoded ending printed after it
- [ ] `python3 -m pytest module-2-simple-statements/`

## Module 3 — Conditional Statements 🔀
- [ ] Two choices shown
- [ ] `if`/`elif` → different outcomes
- [ ] Invalid input handled
- [ ] `python3 -m pytest module-3-conditional-statements/`

## Module 4 — Sequences, Loops, File I/O 🔁
- [ ] Scenes in a list
- [ ] `while` loop, scene to scene
- [ ] Writes ending to a file
- [ ] Reads file back on next run
- [ ] `python3 -m pytest module-4-sequences-loops-fileio/`

## Module 5 — Functions I 🧩
- [ ] `show_scene()` extracted from `main()`
- [ ] `get_choice()` extracted from `main()`
- [ ] Same behavior as Module 4
- [ ] `python3 -m pytest module-5-user-defined-functions-1/`

## Module 6 — Functions II ✂️
- [ ] Short, readable `main()`
- [ ] Each function, one clear job
- [ ] Same behavior as Module 5
- [ ] `python3 -m pytest module-6-user-defined-functions-2/`

## Module 7 — Multi-Dimensional Lists 📊
- [ ] Tracked stat added (syllabus: structured data that updates — e.g. budget, energy)
- [ ] At least one choice modifies it
- [ ] `python3 -m pytest module-7-multidimensional-lists/`
- [ ] *(AI tools OK from here — see README)*

## Module 8 — Dictionaries 🗃️
- [ ] Story as `scene_id -> {text, choices}`
- [ ] Loop reads from dict, not hardcoded branches
- [ ] New scene = edit dict only
- [ ] `python3 -m pytest module-8-dictionaries/`

## Module 9 — Classes 💾
- [ ] `Player`: name, scene, stats
- [ ] JSON save after each choice
- [ ] Quit and resume where you left off
- [ ] `python3 -m pytest module-9-classes/`

---

**All 9 done?** 🎉 Playable, saveable CYOA — built by you. That's the project.
