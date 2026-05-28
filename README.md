# Password Policy Testing & Credential Security Assessment Toolkit

## Overview
This toolkit provides a practical, ethical environment for understanding password cracking, credential storage, and security assessment. It is designed for both red team (offensive) and blue team (defensive) learning.

## Features
- **Dictionary Generator**: Custom wordlist creation with mutation rules
- **Hash Extraction**: Extracts hashes from Linux shadow and Windows SAM files
- **Brute-Force Simulator**: Simulates password cracking attempts
- **Password Strength Analyzer**: Analyzes password complexity and entropy
- **Report Generation**: Summarizes findings and recommendations

## Project Structure
- `main.py`: Entry point and CLI
- `dictionary_generator.py`: Wordlist generation logic
- `hash_extractor.py`: Hash extraction logic
- `bruteforce_simulator.py`: Brute-force and dictionary attack simulation
- `password_analyzer.py`: Password strength analysis
- `report_generator.py`: Audit report creation
- `utils.py`: Shared helpers
- `/docs`: Documentation and diagrams
- `/samples`: Sample input files
- `/output`: Generated wordlists, reports, results

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Usage
1. Run `main.py` and follow the menu prompts.
2. Place sample data in `/samples` as needed.
3. Outputs and reports are saved in `/output`.

## Ethical Notice
Use this toolkit only in controlled, ethical environments. Do not use on unauthorized systems.
