"""
Report Generator Module
Generates audit reports based on analysis and simulation results.
"""
def generate_report():
    import os
    analysis_path = os.path.join(os.path.dirname(__file__), 'output', 'password_analysis.txt')
    bruteforce_path = os.path.join(os.path.dirname(__file__), 'output', 'bruteforce_results.txt')
    report_path = os.path.join(os.path.dirname(__file__), 'output', 'final_audit_report.txt')
    report = []
    # Summary of weak passwords
    if os.path.exists(analysis_path):
        with open(analysis_path, 'r') as infile:
            weak = [line for line in infile if 'Weak' in line]
        report.append(f"Weak Passwords Found: {len(weak)}")
        report.extend(weak)
    else:
        report.append("No password analysis found.")
    # Brute-force results
    if os.path.exists(bruteforce_path):
        report.append("\nBrute-Force Simulation Results:")
        with open(bruteforce_path, 'r') as infile:
            report.extend([line.strip() for line in infile])
    else:
        report.append("No brute-force results found.")
    # Recommendations
    report.append("\nRecommendations:")
    report.append("- Use passwords with at least 12 characters, including upper, lower, digits, and symbols.")
    report.append("- Avoid dictionary words and common patterns.")
    report.append("- Enforce regular password changes and audit policies.")
    with open(report_path, 'w') as outfile:
        for line in report:
            outfile.write(line if line.endswith('\n') else line + '\n')
    print(f"Final audit report generated at {report_path}")
