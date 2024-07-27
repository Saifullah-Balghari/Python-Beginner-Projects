from tkinter import messagebox
import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.build_ui()

    def build_ui(self):
        self.root = tk.Tk()
        self.root.geometry("350x400")
        self.root.title("Arithmetic Calculator")
        self.equation_text = ""
        self.equation_label = tk.StringVar()

        label = tk.Label(self.root, textvariable=self.equation_label, font=('Helvetica', 30), anchor="e", bg='black', fg='white', height=2)
        label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        frame = tk.Frame(self.root, bg='black')
        frame.grid(row=1, column=0, columnspan=4, sticky='nsew')

        number_button_config = {
            'height': 2, 'font': ('Helvetica', 20, 'bold'), 'relief': tk.RAISED, 'bg': '#505050',
            'fg': 'white', 'activebackground': '#606060', 'activeforeground': 'white'
        }
        operator_button_config = {
            'height': 2, 'font': ('Helvetica', 20, 'bold'), 'relief': tk.RAISED, 'bg': '#FF9500',
            'fg': 'white', 'activebackground': '#FFB84D', 'activeforeground': 'white'
        }
        special_button_config = {
            'height': 2, 'font': ('Helvetica', 20, 'bold'), 'relief': tk.RAISED, 'bg': '#D4D4D2',
            'fg': 'black', 'activebackground': '#E5E5E2', 'activeforeground': 'black'
        }

        buttons = [
            ('M+', self.memory_add, 1, 0, special_button_config),
            ('M-', self.memory_subtract, 1, 1, special_button_config),
            ('MR', self.memory_recall, 1, 2, special_button_config),
            ('MC', self.memory_clear, 1, 3, special_button_config),
            ('C', self.clear, 2, 0, special_button_config),
            ('√', self.square_root, 2, 3, operator_button_config),
            ('^', lambda: self.button_press('**'), 2, 2, operator_button_config),
            ('+', lambda: self.button_press('+'), 6, 3, operator_button_config),
            (1, lambda: self.button_press(1), 3, 0, number_button_config),
            (2, lambda: self.button_press(2), 3, 1, number_button_config),
            (3, lambda: self.button_press(3), 3, 2, number_button_config),
            ('-', lambda: self.button_press('-'), 3, 3, operator_button_config),
            (4, lambda: self.button_press(4), 4, 0, number_button_config),
            (5, lambda: self.button_press(5), 4, 1, number_button_config),
            (6, lambda: self.button_press(6), 4, 2, number_button_config),
            ('*', lambda: self.button_press('*'), 4, 3, operator_button_config),
            (7, lambda: self.button_press(7), 5, 0, number_button_config),
            (8, lambda: self.button_press(8), 5, 1, number_button_config),
            (9, lambda: self.button_press(9), 5, 2, number_button_config),
            ('/', lambda: self.button_press('/'), 5, 3, operator_button_config),
            (0, lambda: self.button_press(0), 6, 0, number_button_config),
            ('.', lambda: self.button_press('.'), 6, 1, number_button_config),
            ('=', self.equals, 6, 2, operator_button_config),
            ('Del', self.backspace, 2, 1, special_button_config)
        ]

        for (text, command, row, col, config) in buttons:
            tk.Button(frame, text=text, command=command, **config).grid(row=row, column=col, sticky='nsew')

        for i in range(1, 7):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        
        self.memory = 0
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=10)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.mainloop()

    def button_press(self, num):
        self.equation_text += str(num)
        self.equation_label.set(self.equation_text)

    def equals(self):
        try:
            self.total = str(eval(self.equation_text))
            self.equation_label.set(self.total)
            self.equation_text = self.total
        except SyntaxError:
            self.equation_label.set("Syntax Error!")
            self.equation_text = ""
        except ZeroDivisionError:
            self.equation_label.set("Math Error!")
            self.equation_text = ""
        except Exception as e:
           messagebox.showerror("Error", str(e))
           self.equation_label.set("")
           self.equation_text = ""

    def clear(self):
        self.equation_label.set("")
        self.equation_text = ""

    def backspace(self):
        self.equation_text = self.equation_text[:-1]
        self.equation_label.set(self.equation_text)

    def square_root(self):
        try:
            self.total = str(math.sqrt(eval(self.equation_text)))
            self.equation_label.set(self.total)
            self.equation_text = self.total
        except Exception as e:
           messagebox.showerror("Error", str(e))
           self.equation_label.set("")
           self.equation_text = ""

    def memory_add(self):
        try:
            self.memory += eval(self.equation_text)
        except Exception as e:
           messagebox.showerror("Error", str(e))
           self.equation_label.set("")
           self.equation_text = ""

    def memory_subtract(self):
        try:
            self.memory -= eval(self.equation_text)
        except Exception as e:
           messagebox.showerror("Error", str(e))
           self.equation_label.set("")
           self.equation_text = ""

    def memory_recall(self):
        self.equation_text = str(self.memory)
        self.equation_label.set(self.equation_text)

    def memory_clear(self):
        self.memory = 0

if __name__ == "__main__":
    calculator = Calculator()
