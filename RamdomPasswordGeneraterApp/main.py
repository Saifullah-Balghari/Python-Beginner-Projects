import tkinter as tk
from tkinter import messagebox
import random
import string

class RandomPasswordGeneratorApp:
    
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.length = tk.IntVar(value=12)
        self.gui()
        self.root.mainloop()
    
    def gui(self) -> None:

        self.root.title("Random password generator").title()
        self.root.geometry("200x250")
        
        self.password_label = tk.Label(self.root, text="", width="20", height="2", relief="sunken")
        self.password_label.pack()

        self.lowerCaseCheckBoxVar = tk.BooleanVar()
        self.lowerCaseCheckBox = tk.Checkbutton(self.root, text="LowerCase", variable=self.lowerCaseCheckBoxVar)
        self.lowerCaseCheckBox.pack()

        self.upperCaseCheckBoxVar = tk.BooleanVar()
        self.upperCaseCheckBox = tk.Checkbutton(self.root, text="UpperCase", variable=self.upperCaseCheckBoxVar)
        self.upperCaseCheckBox.pack()

        self.numbersCheckBoxVar = tk.BooleanVar()
        self.numbersCheckBox = tk.Checkbutton(self.root, text="Numbers", variable=self.numbersCheckBoxVar)
        self.numbersCheckBox.pack()

        self.symbolsCheckBoxVar = tk.BooleanVar()
        self.symbolsCheckBox = tk.Checkbutton(self.root, text="Symbols", variable=self.symbolsCheckBoxVar)
        self.symbolsCheckBox.pack()

        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.root, textvariable=self.length)
        self.length_entry.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generator)
        self.generate_button.pack()
        
    def generator(self) -> None:
        self.characters = ""
        if self.lowerCaseCheckBoxVar.get():
            self.characters += string.ascii_lowercase

        if self.upperCaseCheckBoxVar.get():
            self.characters += string.ascii_uppercase

        if self.numbersCheckBoxVar.get():
            self.characters += string.digits

        if self.symbolsCheckBoxVar.get():
            self.characters += string.punctuation

        if not self.characters:
            messagebox.showinfo("Error", "You must select at least one option!")
            return None    
            
        password_length = self.length.get()
        password = "".join(random.choice(self.characters) for _ in range(password_length))
        self.password_label.config(text=password)

def main():

    RandomPasswordGeneratorApp()

if __name__=="__main__":
    main()
