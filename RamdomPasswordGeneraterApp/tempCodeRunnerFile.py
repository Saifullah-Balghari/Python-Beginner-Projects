import tkinter as tk
from tkinter import messagebox

# Create a Tkinter window
root = tk.Tk()
root.title("Tkinter Messagebox Example")

# Function to display the messagebox
def show_messagebox():
    messagebox.showinfo("Message", "This is a Tkinter messagebox example.")

# Create a button to trigger the messagebox
button = tk.Button(root, text="Show Messagebox", command=show_messagebox)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
