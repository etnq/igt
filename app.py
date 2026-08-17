import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()


print("Instagram Script")
def display_list():
    items = ["Python", "JavaScript", "C++", "Rust", "Go"]
    
    print("\n--- Programming Languages List ---")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
    print("----------------------------------\n")

if __name__ == "__main__":
    display_list()
