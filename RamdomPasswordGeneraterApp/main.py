import tkinter as tk
import random
import string

class RandomPasswordGeneratorApp:
    def __init__(self) -> None:
        
        root = tk.Tk()
        root.title("Random password generator").title()
        root.mainloop()
    
    def generator(self, uppercase: bool, lowercase: bool, numbers: bool, symbols: bool, length: int) -> None:
        characters = ""
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if numbers:
            characters += string.digits
        if symbols:
            characters += string.punctuation
        if not characters:
            print("You're password should at least contains any one of the above!")
            return None
        
        password = "".join(random.choice(characters) for _ in range(length))

        return password

def main():        
    RandomPasswordGeneratorApp()

if __name__=="__main__":
    main()
