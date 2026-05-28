"""
Main CLI for Password Policy Testing & Credential Security Assessment Toolkit
"""
from dictionary_generator import generate_dictionary
from hash_extractor import extract_hashes
from bruteforce_simulator import simulate_bruteforce
from password_analyzer import analyze_passwords
from report_generator import generate_report

import sys

def main():
    while True:
        print("""
Password Security Toolkit
========================
1. Generate Dictionary
2. Extract Hashes
3. Simulate Brute-Force Attack
4. Analyze Password Strength
5. Generate Audit Report
6. Exit
""")
        choice = input("Select an option: ")
        if choice == '1':
            generate_dictionary()
        elif choice == '2':
            extract_hashes()
        elif choice == '3':
            simulate_bruteforce()
        elif choice == '4':
            analyze_passwords()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
