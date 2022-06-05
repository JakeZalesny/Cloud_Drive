"""
UI 

ARGS: NONE
RTRNS: User Choice

"""

class UI: 
    def __init__(self) -> None:
        self.choice = None
    
    def display_UI(self):
        print(""" 1. Add File\n 2. Delete File\n 3. Download File\n 4. Check Log\n 5. Quit\n""")
    
    def get_choice(self):
        self.choice = int(input("> "))
        return self.choice