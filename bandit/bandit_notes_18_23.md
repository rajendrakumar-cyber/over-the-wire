# OverTheWire Bandit: Levels 18 → 23 Notes

This document summarizes the steps taken to solve Bandit Levels 18 through 23.

---

## 🛠️ Bandit Level 18 → Level 19

### Goal
Log in as `bandit18` and retrieve the password stored in `readme` in the home directory. The login shell for `bandit18` is configured to log out immediately upon connection.

### Steps
1. **Bypassing the Interactive Shell restriction**:
   When connecting to the server interactively via SSH, the session is terminated immediately. To bypass this, specify the command to execute directly at the end of the SSH command:
   ```bash
   ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
   ```
2. **Retrieved Password**:
   Entering the `bandit18` password (`x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`) triggers the command `cat readme` and yields:
   ```
   cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
   ```

---

## 🛠️ Bandit Level 19 → Level 20

### Goal
Retrieve the password for the next level stored in `/etc/bandit_pass/bandit20` using a SetUID binary.

### Steps
1. **Inspect Directory**:
   Log in as `bandit19` and list the home directory:
   ```bash
   ls -la
   ```
   Output shows a file named `bandit20-do`.

2. **Check Permissions**:
   ```bash
   ls -ltr bandit20-do
   # Output: -rwsr-x--- 1 bandit20 bandit19 14888 Apr  3 15:17 bandit20-do
   ```
   The presence of `s` in the owner execution permission indicates the **SetUID** bit is set. The owner is `bandit20`, which means the binary executes with `bandit20` privileges.

3. **Running the Binary**:
   Run `./bandit20-do` without arguments to see the usage instructions:
   ```
   Run a command as another user.
     Example: ./bandit20-do whoami
   ```
   Running `./bandit20-do whoami` outputs `bandit20`.

4. **Retrieved Password**:
   Execute the `cat` command on the password file using the binary:
   ```bash
   ./bandit20-do cat /etc/bandit_pass/bandit20
   ```
   **Password**:
   ```
   0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
   ```

---

## 🛠️ Bandit Level 20 → Level 21

### Goal
Connect to a local port via TCP, send the current level's password, and receive the next password in response using the SetUID binary `suconnect`.

### Steps
1. **Analyze Binary**:
   Log in as `bandit20` and check the home directory:
   ```bash
   ls -la
   # Output: -rwsr-x--- 1 bandit21 bandit20 15612 Apr  3 15:17 suconnect
   ```
   `suconnect` is a SetUID binary owned by `bandit21`. Running it prints:
   ```
   Usage: ./suconnect <portnumber>
   This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
   ```

2. **Listening on a Port**:
   Open a terminal and start listening on an arbitrary TCP port (e.g., `9999`) using `netcat`:
   ```bash
   nc -lvp 9999
   ```

3. **Triggering the connection**:
   In another terminal session on the same server, run `suconnect` pointing to the listener port:
   ```bash
   ./suconnect 9999
   ```

4. **Sending the Password**:
   When the connection is established, send the current password (`0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`) through the listener terminal.
   The binary will verify the password and return the password for the next level.

5. **Retrieved Password**:
   ```
   EeoULMCra2q0dSkYj561DX7s1CpBuOBt
   ```

---

## 🛠️ Bandit Level 21 → Level 22

### Goal
Find the password for the next level by inspecting a scheduled `cron` job.

### Steps
1. **Inspect Cron Jobs**:
   Log in as `bandit21` and view the list of cron jobs:
   ```bash
   ls -la /etc/cron.d/
   ```
   We find a cron configuration file named `cronjob_bandit22`.

2. **Read the Cron Job configuration**:
   ```bash
   cat /etc/cron.d/cronjob_bandit22
   # Output:
   # @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
   # * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
   ```
   This means that every minute, the script `/usr/bin/cronjob_bandit22.sh` runs as the user `bandit22`.

3. **Inspect the Script**:
   Read the script being executed:
   ```bash
   cat /usr/bin/cronjob_bandit22.sh
   # Output:
   # #!/bin/bash
   # chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   # cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```
   The script copies the password file `/etc/bandit_pass/bandit22` to `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` and makes it world-readable.

4. **Retrieved Password**:
   Read the contents of the target temporary file:
   ```bash
   cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
   ```
   **Password**:
   ```
   tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
   ```

---

## 🛠️ Bandit Level 22 → Level 23

### Goal
Find the password for the next level by calculating the destination path of another scheduled `cron` job.

### Steps
1. **Inspect Cron Job**:
   Log in as `bandit22` and check the cron config file `cronjob_bandit23`:
   ```bash
   cat /etc/cron.d/cronjob_bandit23
   # Output:
   # @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
   # * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
   ```

2. **Inspect the Script**:
   ```bash
   cat /usr/bin/cronjob_bandit23.sh
   # Output:
   # #!/bin/bash
   # myname=$(whoami)
   # mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
   # echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
   # cat /etc/bandit_pass/$myname > /tmp/$mytarget
   ```
   This script runs as `bandit23`. It calculates an MD5 checksum of the string `"I am user bandit23"` and uses that hash as the filename in `/tmp/` to dump the password.

3. **Replicate the Calculation**:
   Calculate the MD5 checksum of the target string manually:
   ```bash
   echo I am user bandit23 | md5sum | cut -d ' ' -f 1
   # Output: 8ca319486bfbbc3663ea0fbe81326349
   ```

4. **Retrieved Password**:
   Read the output file using the calculated hash:
   ```bash
   cat /tmp/8ca319486bfbbc3663ea0fbe81326349
   ```
   **Password**:
   ```
   0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
   ```
