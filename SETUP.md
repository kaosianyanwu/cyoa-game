# 🛠️ Setup Guide

Get your tools working before any game code. Broken setup makes everything feel harder than it is.

---

## 1. 🐍 Install Python

```bash
python3 --version
```

`Python 3.11.x` or higher? Jump to step 2.

If not:
- **Mac:** [python.org/downloads](https://www.python.org/downloads/) or `brew install python3`
- **Windows:** [python.org/downloads](https://www.python.org/downloads/) — check **"Add Python to PATH"**

Confirm in a **new** terminal: `python3 --version`

---

## 2. 📦 Install Git

```bash
git --version
```

If not:
- **Mac:** `xcode-select --install` or [git-scm.com](https://git-scm.com/downloads)
- **Windows:** [git-scm.com](https://git-scm.com/downloads)

One-time setup:

```bash
git config --global user.name "Your Name"
git config --global user.email "the-email-on-your-github-account"
```

---

## 3. 🔑 GitHub login

Pick one:

**Option A — easiest:** [GitHub Desktop](https://desktop.github.com/)

**Option B — terminal:** [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) or [SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

## 4. 💻 Editor

[cursor.com](https://www.cursor.com/) or [code.visualstudio.com](https://code.visualstudio.com/)

---

## 5. 📥 Clone the repo

Accept Kaosi's collaborator invite first, then:

```bash
git clone https://github.com/kaosianyanwu/cyoa-game.git
cd cyoa-game
```

---

## 6. 📚 Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## 7. ✅ Verify

Module 1 tests should **fail** — you haven't coded yet. You're checking the tools run:

```bash
python3 -m pytest module-1-introduction/test_module1.py -v
```

Test output (even red ❌ failures)? Setup worked. `command not found`? Stop and flag it.

**Optional — run everything once:**

```bash
python3 -m pytest -v
```

You'll see a mix of pass and fail. **That's normal.** Starters are mostly `# TODO` — many tests only pass after *you* write the code for that module. Don't panic at red tests on day one; you fix them one module at a time.

---

> **Stuck 15+ min?** Message Kaosi with the exact error. Setup help is always fair game.

**Ready?** [TASKS.md](TASKS.md) + fill out [GAME_PLAN.md](GAME_PLAN.md).
