# 🚀 Submitting a PR

Code done, tests green, explain-your-code written? Ship it.

---

## 1. 🌿 Own branch

At the **start** of each module (forgot? message Kaosi):

```bash
git checkout main
git pull
git checkout -b module-1-yourname
```

Use `module-N-yourname` so Kaosi knows who and which module.

---

## 2. 💾 Commit

```bash
git add .
git commit -m "Complete module 1"
```

---

## 3. ☁️ Push

```bash
git push -u origin module-1-yourname
```

`-u origin ...` only the first push on a branch — then plain `git push`.

---

## 4. 📝 Open the PR

1. [github.com/kaosianyanwu/cyoa-game](https://github.com/kaosianyanwu/cyoa-game)
2. Yellow banner **"Compare & pull request"** → click it  
   *(No banner? Pull requests → New → base `main`, compare your branch)*
3. **Title:** `Module 1: Introduction`
4. **Description:** your explain-your-code note
5. **Reviewers** → gear → **kaosianyanwu**
6. **Create pull request**

---

## 5. 💬 Ping Kaosi

**"Module N done, ready for a PR"** + link. GitHub notifies her too — the message is backup.

---

## 6. 🔄 After review

Fix on the same branch, push — PR updates automatically:

```bash
git checkout module-1-yourname
git add .
git commit -m "Address review feedback"
git push
```

Merged? Next module:

```bash
git checkout main
git pull
git checkout -b module-2-yourname
```

Copy your merged `game.py` into the new module folder before you code.

---

> No new PR for fixes — same branch, same PR.
