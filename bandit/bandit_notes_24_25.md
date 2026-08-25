# OverTheWire Bandit: Level 24 → 25 Notes

## 🛠️ Bandit Level 24 → Level 25

### Goal
Brute-force a 4-digit PIN for a daemon listening on port 30002. The service requires the `bandit24` password followed by the PIN.

### Password for bandit24
`gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

### Strategy
Since we can send multiple attempts over a single connection, we can use a bash loop to generate all possible PINs (0000 to 9999) and pipe them directly into `netcat`.

### Password Retrieved
**bandit25**: `iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`
