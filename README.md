# Failed Login Analyzer

This project provides a simple Python script to analyze failed SSH login attempts on a CentOS (or other Linux) system by parsing the `/var/log/secure` log file.

## 📌 Features

- Extracts IP addresses or hostnames from failed login attempts
- Counts and displays the number of failed attempts per source
- Helps system administrators quickly identify brute-force attack patterns

## 🛠️ Requirements

- Python 3.x
- Linux system with access to `/var/log/secure` (e.g., CentOS, RHEL)

## 📂 File Structure
failed-login-analyzer/ ├── analyze_failed_logins.py # Main Python script ├── failed_logins.txt # Generated log of failed attempts (from grep)


## 🚀 How to Use

1. Extract failed login entries from `/var/log/secure`:

```bash
sudo grep "Failed password" /var/log/secure > failed_logins.txt

