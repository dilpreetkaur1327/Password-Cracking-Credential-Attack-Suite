# Toolkit Architecture & Workflow

## Flowchart (Text Version)

START
↓
Input Data → Generate Dictionary
↓
Extract Password Hashes
↓
Simulate Dictionary/Brute-Force Attack
↓
Analyze Password Strength
↓
Generate Final Audit Report
↓
END

## Module Descriptions
- **Dictionary Generator**: Builds wordlists from user data, patterns, and mutations.
- **Hash Extractor**: Extracts hashes from Linux/Windows files, identifies hash types.
- **Brute-Force Simulator**: Simulates attacks, estimates time-to-crack.
- **Password Analyzer**: Checks complexity, entropy, and dictionary weaknesses.
- **Report Generator**: Summarizes findings, risks, and recommendations.

## Data Flow
1. User provides input (usernames, sample passwords, or hash files).
2. Dictionary is generated and/or imported.
3. Hashes are extracted (optional, for demo/controlled use).
4. Brute-force and dictionary attacks are simulated.
5. Passwords are analyzed for strength and weaknesses.
6. A report is generated with results and recommendations.

## Technologies Used
- Python 3.8+
- hashlib, passlib
- (Optional) crypt, reg.exe, John the Ripper/Hashcat (reference)

## Ethical Use
- Only use in controlled, authorized environments.
- Do not use on real/production systems without permission.
