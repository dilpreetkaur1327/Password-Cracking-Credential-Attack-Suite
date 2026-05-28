"""
Brute-Force Simulator Module
Simulates brute-force and dictionary attacks.
"""
def simulate_bruteforce():
    import os
    import time
    from passlib.hash import sha512_crypt, sha256_crypt, md5_crypt
    input_hashes = os.path.join(os.path.dirname(__file__), 'output', 'extracted_hashes.txt')
    wordlist_path = os.path.join(os.path.dirname(__file__), 'output', 'wordlist.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output', 'bruteforce_results.txt')
    if not os.path.exists(input_hashes) or not os.path.exists(wordlist_path):
        print("Required files not found. Run dictionary and hash extraction first.")
        return
    # Read hashes
    hashes = []
    with open(input_hashes, 'r') as infile:
        for line in infile:
            if ':' in line:
                username, rest = line.strip().split(':', 1)
                hash_field = rest.split(' [')[0]
                hashes.append((username, hash_field))
    # Read wordlist
    with open(wordlist_path, 'r') as infile:
        words = [line.strip() for line in infile if line.strip()]
    results = []
    start_time = time.time()
    for username, hash_field in hashes:
        found = False
        for word in words:
            # Only support SHA-512, SHA-256, MD5 for demo
            if hash_field.startswith('$6$'):
                if sha512_crypt.verify(word, hash_field):
                    found = True
                    break
            elif hash_field.startswith('$5$'):
                if sha256_crypt.verify(word, hash_field):
                    found = True
                    break
            elif hash_field.startswith('$1$'):
                if md5_crypt.verify(word, hash_field):
                    found = True
                    break
        elapsed = time.time() - start_time
        if found:
            results.append(f"{username}: Password cracked! ({word}) in {elapsed:.2f}s")
        else:
            results.append(f"{username}: Not cracked (wordlist only)")
    with open(output_path, 'w') as outfile:
        for line in results:
            outfile.write(line + '\n')
    print(f"Brute-force simulation complete. Results saved to {output_path}")
