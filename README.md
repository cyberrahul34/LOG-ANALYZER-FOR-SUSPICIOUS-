# LOG-ANALYZER-FOR-SUSPICIOUS-


# SUSPICIOU
## Log Analyzer for Suspicious Activity

A Python-based cybersecurity project that analyzes system logs and detects suspicious login activities, including repeated failed login attempts.

## 👨‍💻 Developer Details

- **Name:** Rahul Kumar
- **Course:** Cyber Security
- **Qualification:** BCA
- **Project Name:** SUSPICIOU

## 📌 Project Overview

Every computer system generates log files containing information about login attempts and system activities.

Manually checking large log files is time-consuming. This project automatically scans authentication logs, identifies failed login attempts, counts attempts from each IP address, and flags suspicious IPs.

## 🎯 Project Objectives

- Read system authentication log files.
- Detect repeated failed login attempts.
- Extract IP addresses using Regular Expressions.
- Count failed attempts for each IP.
- Identify suspicious IP addresses.
- Generate a security report automatically.

## ✨ Features

- Log file parsing
- Failed login detection
- IP address extraction
- IP-wise attempt counting
- Suspicious IP detection
- Automatic report generation

## 🛠️ Technologies Used

- Python
- Regular Expressions (re)
- Collections Counter
- Pathlib
- File Handling
- Visual Studio Code

## 📂 Project Structure

SUSPICIOU/
│
├── Log analyzer.py
├── auth.log
├── suspicious_report.txt
└── README.md

## ⚙️ Detection Logic

The project uses a threshold of 5 failed login attempts.

- 1–5 attempts: SAFE under the configured rule
- More than 5 attempts: SUSPICIOUS

Example:

192.168.1.15 - 6 failed attempts

Status: SUSPICIOUS

## 🚀 How to Run

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open Project Folder

Open the project folder in VS Code.

### Step 3: Run the Program

Open the VS Code terminal and execute:

python "Log analyzer.py"

### Step 4: View Results

The program displays suspicious IP addresses in the terminal.

It also generates:

suspicious_report.txt

## 📊 Sample Output

SUSPICIOU SECURITY REPORT

192.168.1.10 - 1 attempts - SAFE

192.168.1.15 - 6 attempts - SUSPICIOUS

10.0.0.25 - 1 attempts - SAFE

Total IPs: 3

Suspicious IPs: 1

Report saved successfully!

## 🔮 Future Enhancements

- Real-time log monitoring
- Graphical user interface (GUI)
- Email security alerts
- Time-based brute-force detection
- CSV report generation
- IP address validation

## ⚠️ Limitations

- Current detection counts attempts across the complete log file.
- It does not detect attacks using a time window.
- It does not automatically block suspicious IP addresses.
- Results depend on the supported log format.

## 🎓 Learning Outcomes

This project helped me understand:

- Python programming
- File handling
- Regular Expressions
- Data counting using Counter
- Basic cybersecurity concepts
- Authentication log analysis

## 👨‍💻 Author

**Rahul Kumar**

Cyber Security | BCA

Project: SUSPICIOU – Log Analyzer for Suspicious Activity
