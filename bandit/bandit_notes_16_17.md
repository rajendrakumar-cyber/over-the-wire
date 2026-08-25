# OverTheWire Bandit: Levels 16 & 17 Notes

This document summarizes the steps taken to solve Bandit Levels 16 and 17.

---

## 🛠️ Bandit Level 16 → Level 17

### Goal
Submit the password of Level 15 (`kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`) to the single listening port in the range `31000` to `32000` that speaks SSL/TLS and returns the next credentials (a private SSH key).

### Steps
1. **Port Scanning**:
   Identify which ports in the range `31000` to `32000` are listening:
   ```bash
   nmap -p 31000-32000 localhost
   ```
   **Output**: Found 5 open ports: `31046`, `31518`, `31691`, `31790`, `31960`.

2. **Service & SSL/TLS Verification**:
   Scan the open ports with version detection to see which speak SSL/TLS:
   ```bash
   nmap -p 31046,31518,31691,31790,31960 -A localhost
   ```
   * Port `31518` runs `ssl/echo` (simply echoes back).
   * Port `31790` runs `ssl/unknown` and returns `Wrong! Please enter the correct current password.` when probed.

3. **Retrieving the Key**:
   Connect to port `31790` using `openssl` and submit the Level 15 password:
   ```bash
   echo kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx | openssl s_client -connect localhost:31790 -quiet
   ```
   **Result**: The server accepted the password and returned an RSA Private Key.

4. **Saving the SSH Key**:
   * Save the private key to a local file named `bandit17.key`.
   * Set secure permissions so SSH will allow its use:
     ```bash
     chmod 600 bandit17.key
     ```

---

## 🛠️ Bandit Level 17 → Level 18

### Goal
Find the password for Level 18 inside `passwords.new` in the home directory. It is the only line that has been changed between `passwords.old` and `passwords.new`.

### Steps
1. **Comparing the Files**:
   Since the server has `diff` installed, compare the contents of the old and new password files:
   ```bash
   diff passwords.old passwords.new
   ```

2. **Analyzing the Diff**:
   ```diff
   42c42
   < 390zFj2NETFVZkqYw8UEFdN6h40oGVtT
   ---
   > x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
   ```
   * The line prefixed with `<` represents `passwords.old`.
   * The line prefixed with `>` represents `passwords.new`.

3. **Retrieved Password**:
   The changed password in `passwords.new` (Level 18 credentials) is:
   ```
   x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
   ```
