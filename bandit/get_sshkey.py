import pexpect
import sys

def get_sshkey():
    password = "iCi86ttT4KSNe1armKiwbQNmB3YJP3q4"
    user = "bandit25"
    host = "bandit.labs.overthewire.org"
    port = 2220

    child = pexpect.spawn(f"ssh -o StrictHostKeyChecking=no {user}@{host} -p {port}", dimensions=(24, 80))
    # child.logfile = sys.stdout.buffer

    try:
        child.expect("password:", timeout=10)
        child.sendline(password)
        child.expect(r"bandit25@bandit:.*\$", timeout=10)
        
        child.sendline("cat bandit26.sshkey")
        child.expect(r"bandit25@bandit:.*\$", timeout=10)
        key = child.before.decode()
        # Clean up the key
        lines = key.splitlines()
        # The first line is likely the 'cat' command echoing back
        key_content = "\n".join(lines[1:])
        print(key_content)
        
        child.sendline("exit")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    get_sshkey()
