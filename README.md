
# FTP Cracker Tool

A Python-based tool to perform brute-force attacks on FTP servers by testing username and password combinations.

---

## 📋 Project Description

This tool tries different username-password combinations to crack FTP server credentials.
It includes two versions:
- **Basic FTP Cracker (ftp_brute.py)**: Hardcoded host, user, and password list.
- **Advanced FTP Cracker (advanced_ftp_brute.py)**: Fully customizable through command-line arguments, userlist, wordlist, and password generation.

Both versions use **multithreading** for faster attacks and **color-coded outputs** for better visibility.

---

## 🚀 Features

- Multithreaded brute-force FTP login attempts
- Wordlist or password generation support
- Userlist support (advanced version)
- Colored output using Colorama
- Simple and easy to extend

---

## 🛠️ Prerequisites

- **Python 3.x** installed
- Install required library:
  ```bash
  pip install colorama
  ```
- An accessible FTP server for testing (e.g., vsftpd on localhost)

---

## 📂 Project Structure

```
FTP_Cracker_Project/
|
├── ftp_brute.py              # Basic FTP Cracker
├── advanced_ftp_brute.py      # Advanced FTP Cracker
├── wordlist.txt               # Passwords list
└── userlist.txt               # (Optional) Usernames list
```

---

## 📜 Usage Instructions

### Basic FTP Cracker (ftp_brute.py)

1. Edit `ftp_brute.py` to set:
   - Target `host`
   - Username `user`
   - Password list `wordlist.txt`

2. Run the script:
   ```bash
   python ftp_brute.py
   ```

---

### Advanced FTP Cracker (advanced_ftp_brute.py)

1. Prepare:
   - `wordlist.txt` (passwords)
   - `userlist.txt` (optional usernames)

2. Run the script:
   ```bash
   python advanced_ftp_brute.py --host 127.0.0.1 --userlist userlist.txt --wordlist wordlist.txt --threads 5
   ```

**OR** generate passwords dynamically:
   ```bash
   python advanced_ftp_brute.py --host 127.0.0.1 --generate --length 2 --threads 5
   ```

---

## 📈 How It Works

- Connects to the target FTP server.
- Tries different username-password combinations.
- Multithreads the process for faster brute-force.
- Displays successful credentials in **green**.
- Tracks all attempts with color-coded outputs.

---

## ✨ Example Output

```
[+] Found: testuser:1234
[-] Failed: testuser:pass
[-] Failed: testuser:admin
```

---

## 👨‍💻 Author

**Ankit Chaudhari**  
Cybersecurity Enthusiast | Ethical Hacker | Network Auditor

- **University:** Delhi Skill and Entrepreneurship University
- **Certification:** Certified Ethical Hacker (CEH v12)
- **Skills:** Cybersecurity, Ethical Hacking, Network Auditing, VAPT
- **GitHub:** [@ankitchaudharijj](https://github.com/ankitchaudharijj)
- **LinkedIn:** [Ankit Chaudhari](https://www.linkedin.com/in/ankit-chaudhari-40346b318/)

---

## 📄 License

This project is intended for **educational purposes** and **ethical use only**.  
Unauthorized malicious use is strictly prohibited.

---

# 🛡️ Happy Ethical Hacking! 🚀
