
import re
from collections import Counter
from pathlib import Path

THRESHOLD = 5

# Project folder
folder = Path(__file__).resolve().parent
log_file = folder / "auth.log"
report_file = folder / "suspicious_report.txt"

# Create sample log file if it does not exist
if not log_file.exists():
    sample_logs = """
Failed password for root from 192.168.1.10 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for root from 192.168.1.15 port 2222 ssh2
Failed password for admin from 10.0.0.25 port 2222 ssh2
"""
    log_file.write_text(sample_logs)

# Analyze log file
failed_ips = []
pattern = r"Failed password.*?from\s+(\d{1,3}(?:\.\d{1,3}){3})"

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            failed_ips.append(match.group(1))

# Count IP addresses
counter = Counter(failed_ips)

print("\n================================")
print("     SUSPICIOU SECURITY REPORT")
print("================================")

suspicious = []

for ip, count in sorted(counter.items()):
    if count > THRESHOLD:
        status = "SUSPICIOUS ⚠"
        suspicious.append((ip, count))
    else:
        status = "SAFE"

    print(f"{ip} - {count} attempts - {status}")

# Save report
with open(report_file, "w") as report:
    report.write("SUSPICIOU SECURITY REPORT\n")
    report.write("=========================\n")

    for ip, count in suspicious:
        report.write(f"{ip} - {count} failed attempts\n")

print("\nTotal IPs:", len(counter))
print("Suspicious IPs:", len(suspicious))
print("\nReport saved successfully!")
print("File:", report_file)
