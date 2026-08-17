# app.py
import time

def print_banner():
    # ANSI Color Codes
    YELLOW = "\033[38;5;220m"
    CYAN = "\033[38;5;51m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # Compact "INSTAGRAM SCRIPT" ASCII Banner
    banner = [
        " █ █▄ █ █▀▀ ▀█▀ ▄▀█ █▀▀ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▀█ █ █▀█ ▀█▀ ",
        " █ █ ▀█ ▄█░  █░ █▀█ █▄█ █▀▄ █▀█ █▄▀   ▄█░ ▀█▄ █▀▄ █ █▀▀  █░ ",
    ]

    # Print line 1 Yellow, line 2 Cyan for the 2-tone split
    print(f"{YELLOW}{banner[0]}{RESET}")
    print(f"{CYAN}{banner[1]}{RESET}\n")

    # Author Box
    print(f"{YELLOW}           +-+-+-+-+-+-+-+-+-+{RESET}")
    print(f"{YELLOW}           |B|Y|-|D|A|R|K|-|S|{RESET}")
    print(f"{YELLOW}           +-+-+-+-+-+-+-+-+-+{RESET}\n")

    # Status Logs
    print(f"{GREEN}[</>] Initializing Instagram Tools...{RESET}")
    print(f"{GREEN}[+] Status: Connected{RESET}\n")

if __name__ == "__main__":
    print_banner()
    

def display_list():
    items = ["Python", "JavaScript", "C++", "Rust", "Go"]
    
    print("\n--- Programming Languages List ---")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
    print("----------------------------------\n")

if __name__ == "__main__":
    display_list()
