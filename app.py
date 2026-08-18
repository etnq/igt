import os
class InstagramScript:
    def __init__(self):
        self.items=["Login", "Exit", "About Page"]
    def clear_terminal(self):
        os.system('cls' if os.name =='nt' 
else 'clear')
    def display_list(self):
        print("\n----Content---")
        for index, item in 
enumerate(self.items, start=1):
    print(f"{index}.{item}")
print("------------------------------\n")
app=InstagramScript()
app.clear_terminal()
print("Instagram Script")
app.display_list()
