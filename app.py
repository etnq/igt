import os

class InstagramScript:
    def __init__(self):
        self.items = ["Login", "Exit", "About Page"]
        self.running = True

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_list(self):
        print("\n----Content---")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        print("------------------------------\n")

    def handle_login(self):
        print("You selected Login")

    def handle_about(self):
        print("About: Instagram Script v1.0")

    def handle_exit(self):
        print("Goodbye!")
        self.running = False  # encapsulated state, no 'break' needed

    def run(self):
        """The class owns the main loop and routing."""
        while self.running:
            self.clear_terminal()
            print("Instagram Script")
            self.display_list()
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.handle_login()
            elif choice == "2":
                self.handle_exit()
            elif choice == "3":
                self.handle_about()
            else:
                print("Invalid choice!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = InstagramScript()
    app.run()
