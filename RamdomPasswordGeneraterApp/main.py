import tkinter as tk
from tkinter import messagebox
import random
import string

class RandomPasswordGeneratorApp:
    
    def __init__(self) -> None:

        self.characters = ""
        self.length = 8
        self.root = tk.Tk()

        self.gui()

        

        self.root.mainloop()
    
    def gui(self) -> None:

        self.password_label = tk.Label(self.root, text="")
        self.password_label.pack()

        self.root.title("Random password generator").title()
        self.root.geometry("300x300")

        self.lowerCaseCheckBoxVar = tk.BooleanVar()
        self.lowerCaseCheckBox = tk.Checkbutton(self.root, text="LowerCase", variable=self.lowerCaseCheckBoxVar, command=self.lowerCase2ru).pack()
        self.lowerCase = self.lowerCaseCheckBoxVar.get()

        self.upperCaseCheckBoxVar = tk.BooleanVar()
        self.upperCaseCheckBox = tk.Checkbutton(self.root, text="UpperCase", variable=self.upperCaseCheckBoxVar, command=self.upperCase2ru).pack()
        self.upperCase = self.upperCaseCheckBoxVar.get()

        self.numbersCheckBoxVar = tk.BooleanVar()
        self.numbersCheckBox = tk.Checkbutton(self.root, text="Numbers", variable=self.numbersCheckBoxVar, command=self.numbers2ru).pack()
        self.numbers = self.numbersCheckBoxVar.get()

        self.symbolsCheckBoxVar = tk.BooleanVar()
        self.symbolsCheckBox = tk.Checkbutton(self.root, text="Symbols", variable=self.symbolsCheckBoxVar, command=self.symbols2ru).pack()
        self.symbols = self.symbolsCheckBoxVar.get()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generator)
        self.generate_button.pack()
        
    def generator(self) -> None:
        
        if self.upperCase == True:
            self.characters += string.ascii_uppercase
        if self.lowerCase == True:
            self.characters += string.ascii_lowercase
        if self.numbers == True:
            self.characters += string.digits
        if self.symbols == True:
            self.characters += string.punctuation
        if not self.characters:
            messagebox.showinfo("Error", "You're password should at least contains any one of the above!")
        
        password = "".join(random.choice(self.characters) for _ in range(self.length))
        self.password_label.config(text=password)
        
    def lowerCase2ru(self):
        if self.lowerCaseCheckBoxVar.get():
            self.lowerCase = True
        else:
            self.lowerCase = False

    def upperCase2ru(self):
        if self.upperCaseCheckBoxVar.get():
            self.upperCase = True
        else:
            self.upperCase = False

    def numbers2ru(self):
        if self.numbersCheckBoxVar.get():
            self.numbers = True
        else:
            self.numbers = False

    def symbols2ru(self):
        if self.symbolsCheckBoxVar.get():
            self.symbols = True
        else:
            self.symbols = False


def main():        

    RandomPasswordGeneratorApp()

if __name__=="__main__":
    main()
