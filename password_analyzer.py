"""
Password Strength Analyzer Module
Analyzes password complexity, entropy, and predictability.
"""
def analyze_passwords():
    import os
    import math
    wordlist_path = os.path.join(os.path.dirname(__file__), 'output', 'wordlist.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output', 'password_analysis.txt')
    if not os.path.exists(wordlist_path):
        print("Wordlist not found. Run dictionary generator first.")
        return
    def entropy(password):
        pool = 0
        if any(c.islower() for c in password): pool += 26
        if any(c.isupper() for c in password): pool += 26
        if any(c.isdigit() for c in password): pool += 10
        if any(not c.isalnum() for c in password): pool += 32
        if pool == 0: return 0
        return round(len(password) * math.log2(pool), 2)
    results = []
    with open(wordlist_path, 'r') as infile:
        for pw in infile:
            pw = pw.strip()
            if not pw:
                continue
            ent = entropy(pw)
            length = len(pw)
            complexity = sum([any(f(pw) for f in [str.islower, str.isupper, str.isdigit, lambda x: not x.isalnum()])])
            verdict = 'Weak'
            if length >= 12 and ent > 50:
                verdict = 'Strong'
            elif length >= 8 and ent > 35:
                verdict = 'Moderate'
            results.append(f"{pw}: Length={length}, Entropy={ent}, Verdict={verdict}")
    with open(output_path, 'w') as outfile:
        for line in results:
            outfile.write(line + '\n')
    print(f"Password analysis complete. Results saved to {output_path}")
