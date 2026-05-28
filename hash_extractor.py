"""
Hash Extraction Module
Extracts password hashes from Linux shadow or Windows SAM files.
"""
def extract_hashes():
    import os
    input_path = os.path.join(os.path.dirname(__file__), 'samples', 'shadow_sample')
    output_path = os.path.join(os.path.dirname(__file__), 'output', 'extracted_hashes.txt')
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return
    hash_types = {'1': 'MD5', '2a': 'Blowfish', '5': 'SHA-256', '6': 'SHA-512'}
    results = []
    with open(input_path, 'r') as infile:
        for line in infile:
            parts = line.strip().split(':')
            if len(parts) < 2:
                continue
            username = parts[0]
            hash_field = parts[1]
            if hash_field in ('*', '!', ''):
                continue
            if hash_field.startswith('$'):
                fields = hash_field.split('$')
                if len(fields) > 2:
                    algo = fields[1]
                    hash_type = hash_types.get(algo, f'Unknown ({algo})')
                else:
                    hash_type = 'Unknown'
            else:
                hash_type = 'DES (legacy)'
            results.append((username, hash_field, hash_type))
    with open(output_path, 'w') as outfile:
        for username, hash_field, hash_type in results:
            outfile.write(f"{username}:{hash_field} [{hash_type}]\n")
    print(f"Extracted {len(results)} hashes to {output_path}")
