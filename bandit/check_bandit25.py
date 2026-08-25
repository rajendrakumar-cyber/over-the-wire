import pexpect
import sys

def check_bandit25():
    password = "iCi86ttT4KSNe1armKiwbQNmB3YJP3q4"
    user = "bandit25"
    host = "bandit.labs.overthewire.org"
    port = 2220

    child = pexpect.spawn(f"ssh -o StrictHostKeyChecking=no {user}@{host} -p {port}", dimensions=(24, 80))
    # child.logfile = sys.stdout.buffer

    try:
        child.expect("password:", timeout=10)
        child.sendline(password)
        child.expect("bandit25@", timeout=10)
        print("Logged in as bandit25")
        
        child.sendline("ls -la")
        child.expect("bandit25@", timeout=10)
        print("Home directory contents:\n", child.before.decode())
        
        child.sendline("cat bandit26.key") # Just in case
        child.expect("bandit25@", timeout=10)
        print("bandit26.key content:\n", child.before.decode())
        
        child.sendline("exit")
    except Exception as e:
        print("Error:", e)
        print("Output:", child.before.decode() if child.before else "None")

if __name__ == "__main__":
    check_bandit25()
