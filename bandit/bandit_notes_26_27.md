# OverTheWire Bandit: Level 26 → 27 Notes

## 🛠️ Bandit Level 26 → Level 27

### Goal
Log in as `bandit26` and find the password for `bandit27`. There is a setuid binary in the home directory that can be used to read the password for `bandit27`.

### SSH Key for bandit26
Found in `bandit25`'s home directory as `bandit26.sshkey`.

### Strategy
1.  **Log in as bandit26**: Use the SSH key obtained from `bandit25`.
2.  **Bypass the restricted shell**:
    - The shell for `bandit26` is `/usr/bin/showtext`.
    - Trigger the `more` pager by using a small terminal window.
    - Press `v` to enter `vi`.
    - In `vi`, run `:set shell=/bin/bash` and then `:shell`.
3.  **Retrieve the password**:
    - Run the setuid binary `./bandit27-do` with the command to read the password file.
    - `./bandit27-do cat /etc/bandit_pass/bandit27`

### Password Retrieved
**bandit27**: `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`
