"""
Brute-Force Simulator Module
Simulates brute-force and dictionary attacks.
"""

import os
import time
import hashlib
import itertools
import string


def detect_hash_type(hash_str):
    hash_str = hash_str.strip()
    if hash_str.startswith('$6$'):
        return 'sha512'
    elif hash_str.startswith('$5$'):
        return 'sha256'
    elif hash_str.startswith('$1$'):
        return 'md5crypt'
    elif hash_str.startswith('$2b$') or hash_str.startswith('$2a$'):
        return 'bcrypt'
    elif len(hash_str) == 32:
        return 'md5'
    elif len(hash_str) == 40:
        return 'sha1'
    elif len(hash_str) == 64:
        return 'sha256raw'
    elif len(hash_str) == 128:
        return 'sha512raw'
    else:
        return 'unknown'


def hash_word(word, algo):
    word = word.strip()
    if algo == 'md5':
        return hashlib.md5(word.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(word.encode()).hexdigest()
    elif algo == 'sha256raw':
        return hashlib.sha256(word.encode()).hexdigest()
    elif algo == 'sha512raw':
        return hashlib.sha512(word.encode()).hexdigest()
    else:
        return None


def dictionary_attack(target_hash, wordlist_path, algo):
    target_hash = target_hash.strip()
    attempts = 0
    start = time.time()

    if not os.path.exists(wordlist_path):
        print(f"  [!] Wordlist not found: {wordlist_path}")
        return None, attempts, 0

    with open(wordlist_path, 'r', errors='ignore') as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            attempts += 1
            hashed = hash_word(word, algo)
            if hashed and hashed == target_hash:
                elapsed = round(time.time() - start, 3)
                return word, attempts, elapsed
            if attempts % 1000 == 0:
                print(f"  [*] Tried {attempts} words...", end='\r')

    elapsed = round(time.time() - start, 3)
    return None, attempts, elapsed


def brute_force_incremental(target_hash, algo, max_length=4):
    charset = string.ascii_lowercase + string.digits
    attempts = 0
    start = time.time()
    MAX_ATTEMPTS = 500000

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            word = ''.join(combo)
            attempts += 1
            hashed = hash_word(word, algo)
            if hashed and hashed == target_hash:
                elapsed = round(time.time() - start, 3)
                return word, attempts, elapsed
            if attempts >= MAX_ATTEMPTS:
                elapsed = round(time.time() - start, 3)
                return None, attempts, elapsed
            if attempts % 5000 == 0:
                print(f"  [*] Tried {attempts} combinations...", end='\r')

    elapsed = round(time.time() - start, 3)
    return None, attempts, elapsed


def estimate_crack_time(charset_size, length, speed=1_000_000):
    combinations = charset_size ** length
    seconds = combinations / speed
    if seconds < 60:
        return f"{round(seconds, 2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds/60, 2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600, 2)} hours"
    else:
        return f"{round(seconds/86400, 2)} days"


def simulate_bruteforce():
    output_path = os.path.join(os.path.dirname(__file__), 'output')
    wordlist_path = os.path.join(os.path.dirname(__file__), 'output', 'wordlist.txt')
    os.makedirs(output_path, exist_ok=True)

    print("\n=== Brute-Force Simulator ===")
    print("1. Dictionary Attack on a password hash")
    print("2. Incremental Brute-Force Attack")
    print("3. Show estimated crack times")
    choice = input("Select mode: ").strip()

    results = []

    if choice == '1':
        print("\n  Supported algorithms: md5, sha1, sha256raw, sha512raw")
        algo = input("  Enter algorithm: ").strip().lower()
        target = input("  Enter hash to crack: ").strip()

        print(f"\n  [*] Starting dictionary attack using {wordlist_path}")
        found, attempts, elapsed = dictionary_attack(target, wordlist_path, algo)

        if found:
            print(f"\n  [+] CRACKED! Password: {found}")
            print(f"  [+] Attempts: {attempts} | Time: {elapsed}s")
            results.append(f"CRACKED | Hash: {target[:20]}... | Password: {found} | Attempts: {attempts} | Time: {elapsed}s")
        else:
            print(f"\n  [-] Not found in wordlist. Attempts: {attempts} | Time: {elapsed}s")
            results.append(f"NOT FOUND | Hash: {target[:20]}... | Attempts: {attempts} | Time: {elapsed}s")

    elif choice == '2':
        print("\n  Supported algorithms: md5, sha1, sha256raw, sha512raw")
        algo = input("  Enter algorithm: ").strip().lower()
        target = input("  Enter hash to crack: ").strip()
        max_len = int(input("  Max password length to try (recommended: 4): ").strip())

        print(f"\n  [*] Starting incremental brute-force (max length {max_len})...")
        found, attempts, elapsed = brute_force_incremental(target, algo, max_len)

        if found:
            print(f"\n  [+] CRACKED! Password: {found}")
            print(f"  [+] Attempts: {attempts} | Time: {elapsed}s")
            results.append(f"CRACKED | Hash: {target[:20]}... | Password: {found} | Attempts: {attempts} | Time: {elapsed}s")
        else:
            print(f"\n  [-] Not cracked within limit. Attempts: {attempts} | Time: {elapsed}s")
            results.append(f"NOT CRACKED | Attempts: {attempts} | Time: {elapsed}s")

    elif choice == '3':
        print("\n  === Estimated Crack Times (at 1M attempts/sec) ===")
        print(f"  4-char lowercase+digits  (36^4):   {estimate_crack_time(36, 4)}")
        print(f"  6-char lowercase+digits  (36^6):   {estimate_crack_time(36, 6)}")
        print(f"  8-char all printable     (95^8):   {estimate_crack_time(95, 8)}")
        print(f"  10-char all printable    (95^10):  {estimate_crack_time(95, 10)}")
        print(f"  12-char all printable    (95^12):  {estimate_crack_time(95, 12)}")
        results.append("Crack time estimates displayed.")

    # Save results
    out_file = os.path.join(output_path, 'bruteforce_results.txt')
    with open(out_file, 'w') as f:
        f.write("Brute-Force Simulation Results\n")
        f.write("=" * 40 + "\n")
        for r in results:
            f.write(r + "\n")
    print(f"\n  [✓] Results saved to {out_file}")
    return results