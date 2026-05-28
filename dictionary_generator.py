"""
Dictionary Generator Module
Generates custom wordlists with mutation rules.
"""
def generate_dictionary():
    import os
    input_path = os.path.join(os.path.dirname(__file__), 'samples', 'usernames.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output', 'wordlist.txt')
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return
    with open(input_path, 'r') as infile:
        usernames = [line.strip() for line in infile if line.strip()]

    def mutate(word):
        # Simple mutations: original, upper, lower, leet, with numbers
        mutations = set()
        mutations.add(word)
        mutations.add(word.upper())
        mutations.add(word.lower())
        mutations.add(word.capitalize())
        # Leet speak
        leet = word.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '5')
        mutations.add(leet)
        # Append numbers
        for n in range(0, 10):
            mutations.add(f"{word}{n}")
        return mutations

    wordlist = set()
    for username in usernames:
        wordlist.update(mutate(username))

    with open(output_path, 'w') as outfile:
        for word in sorted(wordlist):
            outfile.write(word + '\n')
    print(f"Generated wordlist with {len(wordlist)} entries at {output_path}")
