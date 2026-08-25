# OverTheWire Bandit: Levels 27 → 33 Complete Notes

---

## 🛠 Level 27 → 28
**Goal:** Clone a git repository and find the password.
- **Clone Command:**
  ```bash
  git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo
  ```
- **Password (bandit27):** `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`
- **Retrieval:** Read `README` in the cloned repo.
- **Password (bandit28):** `Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`

---

## 🛠 Level 28 → 29
**Goal:** Find a password deleted from the git history.
- **Clone Command:**
  ```bash
  git clone ssh://bandit28-git@bandit.labs.overthewire.org:2220/home/bandit28-git/repo
  ```
- **Strategy:** Use `git log -p` or `git checkout` to see previous versions of `README.md`.
- **Command Used:** `git checkout a3437bd`
- **Password (bandit29):** `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

---

## 🛠 Level 29 → 30
**Goal:** Find a password stored in a different git branch.
- **Clone Command:**
  ```bash
  git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo
  ```
- **Strategy:** List all branches and switch to the development branch.
- **Commands:**
  ```bash
  git branch -a
  git checkout dev
  ```
- **Password (bandit30):** `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`

---

## 🛠 Level 30 → 31
**Goal:** Find a password stored in a git tag.
- **Clone Command:**
  ```bash
  git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo
  ```
- **Strategy:** List tags and show the content of the secret tag.
- **Commands:**
  ```bash
  git tag
  git show secret
  ```
- **Password (bandit31):** `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

---

## 🛠 Level 31 → 32
**Goal:** Push a file to the remote repository to trigger a hook.
- **Task:** Create `key.txt` with content `'May I come in?'` and push it.
- **Strategy:** Use `git add -f` to bypass `.gitignore`.
- **Commands:**
  ```bash
  echo "May I come in?" > key.txt
  git add -f key.txt
  git commit -m "unlock"
  git push
  ```
- **Password (bandit32):** `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

---

## 🛠 Level 32 → 33
**Goal:** Escape the "UPPERCASE SHELL".
- **Strategy:** Use the `$0` shell variable to execute the original shell (bash).
- **Command:** `$0`
- **Result:** Dropped into a normal shell as `bandit33`.
- **Password (bandit33):** `tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`

---

## 🔑 Summary of Passwords
- **bandit27:** `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`
- **bandit28:** `Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`
- **bandit29:** `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`
- **bandit30:** `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`
- **bandit31:** `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`
- **bandit32:** `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`
- **bandit33:** `tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`
