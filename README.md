# File Integrity Monitor

## Project Overview

The File Integrity Monitor is a Python-based cybersecurity tool designed to detect unauthorized modifications to files by monitoring their cryptographic hash values. The project uses the SHA-256 hashing algorithm to generate a unique digital fingerprint for a file and compares it against a previously stored baseline hash.

This project demonstrates the fundamental principles of file integrity verification and highlights how organizations can detect file tampering, accidental modifications, or potential security breaches.

---

## Project Scope

The scope of this project includes:

* Generation of SHA-256 hash values for files.
* Creation of a baseline hash for integrity verification.
* Detection of file modifications through hash comparison.
* Monitoring file integrity using cryptographic techniques.
* Basic security auditing and tamper detection.
* Demonstration of file integrity monitoring concepts used in cybersecurity.

### Limitations

* Monitors one file at a time.
* Does not provide real-time monitoring.
* Does not automatically restore modified files.
* Does not monitor directories recursively.
* Requires manual execution to perform integrity checks.

---

## Technologies Used

* Python 3
* hashlib Library
* os Library

---

## Features

* Generates SHA-256 hashes for files.
* Creates and stores baseline hash values.
* Detects file modifications and tampering.
* Displays integrity verification results.
* Simple command-line interface.
* Lightweight implementation using built-in Python libraries.

---

## Working Principle

1. The user specifies a file to monitor.
2. The program generates a SHA-256 hash of the file.
3. During the first execution, the hash is stored as a baseline.
4. On subsequent executions, a new hash is generated.
5. The current hash is compared with the stored baseline hash.
6. If both hashes match, file integrity is maintained.
7. If the hashes differ, the file has been modified.

---

## Information Monitored

The File Integrity Monitor verifies:

* File Content Integrity
* SHA-256 Hash Values
* Unauthorized File Modifications
* Changes Between Baseline and Current File State

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd file-integrity-monitor
```

3. No additional packages are required because the project uses Python's built-in libraries.

---

## Usage

Run the program using:

```bash
python file_integrity_monitor.py
```

Enter the file path when prompted:

```text
Enter file path: sample.txt
```

The application will create a baseline hash during the first execution and verify file integrity during subsequent executions.

---

## Sample Output

### First Run

```text
=== File Integrity Monitor ===

Enter file path: sample.txt

Baseline hash created.
Hash: a7f5f35426b927411fc9231b56382173...
```

### Integrity Maintained

```text
Original Hash : a7f5f35426b927411fc9231b56382173...
Current Hash  : a7f5f35426b927411fc9231b56382173...

[OK] File integrity maintained.
```

### File Modified

```text
Original Hash : a7f5f35426b927411fc9231b56382173...
Current Hash  : 4c1f8b6f76d3a87f91e7d...

[ALERT] File has been modified!
```

---

## Educational Objective

The primary objective of this project is to understand:

* File Integrity Monitoring (FIM)
* Cryptographic Hash Functions
* SHA-256 Hashing Algorithm
* Tamper Detection Techniques
* Cybersecurity Monitoring Concepts
* Security Auditing and Verification

---

## Applications

* File Integrity Verification
* Security Monitoring
* Tamper Detection
* Digital Forensics
* Cybersecurity Education
* System Security Auditing

---

## Disclaimer

This project is intended solely for educational and authorized security monitoring purposes. Users should ensure they have permission to monitor and analyze files within their environment. The tool is designed to demonstrate file integrity monitoring concepts and should not be considered a replacement for enterprise-grade security solutions.

---

## Author

**M Hafiza**
**Intern ID:** CITS1108
**Project:** File Integrity Monitor
**Duration:** 8 Weeks
