# Setup Guide

Before touching any code, get these four things working. Don't skip
ahead — if setup is broken, everything after it will be confusing for
the wrong reasons.

## 1. Install Python

Check if you already have it:
```bash
python3 --version
```
If you see something like `Python 3.11.x` or higher, you're set —
skip to Step 2.

If not:
- **Mac:** install from [python.org/downloads](https://www.python.org/downloads/)
  (get the latest 3.x version), or if you have Homebrew: `brew install python3`
- **Windows:** install from [python.org/downloads](https://www.python.org/downloads/).
  During install, check the box that says **"Add Python to PATH"** —
  easy to miss, and things won't work without it.

Verify again with `python3 --version` (Windows: try `python --version`
if `python3` doesn't work).

## 2. Install Git

Check if you already have it:
```bash
git --version
```
If not:
- **Mac:** `xcode-select --install` (installs Git along with Xcode
  command line tools), or [git-scm.com](https://git-scm.com/downloads)
- **Windows:** [git-scm.com](https://git-scm.com/downloads) — use the
  default options during install

Set your identity (one-time, so your commits are attributed to you):
```bash
git config --global user.name "Your Name"
git config --global user.email "the-email-on-your-github-account"
```

## 3. Set up SSH or a login for GitHub

You already have a GitHub account. Now make sure your computer can
push to it — GitHub no longer accepts your account password directly
in the terminal, so pick one:

**Option A — easiest:** Install [GitHub Desktop](https://desktop.github.com/)
and sign in there. It handles authentication for you, and you can still
use the terminal for everything else.

**Option B — terminal-only:** Follow GitHub's guide to set up a
[personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
and use it as your password when prompted, or set up
[SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
for a one-time setup with no repeated logins.

## 4. Install an editor

You'll use Cursor or VS Code to write code. If you don't already have
one: [cursor.com](https://www.cursor.com/) or [code.visualstudio.com](https://code.visualstudio.com/)

## 5. Clone the repo

Once Kaosi shares the repo URL with you and adds you as a collaborator
(check your email/GitHub notifications for the invite — you have to
accept it):

```bash
git clone <REPO_URL_GOES_HERE>
cd cyoa-game
```

## 6. Install project dependencies

```bash
python3 -m pip install -r requirements.txt
```

On Mac, bare `pip` is often not installed — always use `python3 -m pip`.

## 7. Verify everything works

Run the Module 1 tests — they're *supposed* to fail right now, since
you haven't written any code yet. You're just confirming the tools run:
```bash
python3 -m pytest module-1-introduction/test_module1.py -v
```
If you see test output (even failing tests), setup worked. If you see
an error like `command not found` or `no module named pytest`, stop
here and flag it — don't move on with broken tooling.

---

**Stuck at any step?** Don't spend more than 15-20 minutes fighting a
setup issue alone — message Kaosi with the exact error message. Setup
problems are usually quick to fix with a second pair of eyes, and this
is exactly the kind of thing that's fair game to ask about (unlike
game-logic code later on).
