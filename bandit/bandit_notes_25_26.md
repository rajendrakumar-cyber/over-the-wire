# OverTheWire Bandit: Level 25 → 26 Notes

## 🛠️ Bandit Level 25 → Level 26

### Goal
Logging in to `bandit26` from `bandit25` should be fairly easy… The shell for user `bandit26` is not `/bin/bash`, but something else. Find out what it is, how it works and how to break out of it.

### Password for bandit25
`iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

### How the bandit26 Shell Works
1. Inspecting `/etc/passwd` shows that `bandit26` has the login shell `/usr/bin/showtext`.
2. Checking the contents of `/usr/bin/showtext` reveals:
   ```sh
   #!/bin/sh
   export TERM=linux
   exec more ~/text.txt
   exit 0
   ```
   This means that upon login, the user executes `more ~/text.txt` and is immediately logged out when `more` finishes displaying the text.

### Strategy / Breakout Steps
1. **Locate the Key**: Find the SSH private key `bandit26.sshkey` in the home directory of `bandit25`.
2. **Shrink the Terminal**: Shrink the size of your terminal window (e.g., to 5 rows and 50 columns) so that `more` is forced to paginate the text instead of printing it all and exiting.
3. **SSH using the Key**:
   ```sh
   ssh -i bandit26.sshkey bandit26@localhost -p 2220
   ```
4. **Trigger vi from the Pager**: When the `--More--` prompt appears, press `v` to open `vi`.
5. **Breakout from vi**:
   Inside `vi`, run:
   ```
   :set shell=/bin/bash
   :shell
   ```
6. **Retrieve the Password**: Once in the bash shell, run:
   ```sh
   cat /etc/bandit_pass/bandit26
   ```

### Password Retrieved
**bandit26**: `s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ`
