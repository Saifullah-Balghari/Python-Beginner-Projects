import customtkinter as ctk
from difflib import get_close_matches as gcm
from tkinter import messagebox
import tkinter as tk
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ChatBotApp:

    def __init__(self):

        self.file_path = r'/home/sbalghari/Documents/GitHub/Python-Beginner-Projects/ChatBot/memory.json'
        self.memory: dict = self.load_memory()
        self.questions: list | None = [ i ['question'] for i in self.memory['questions']]
        self.user_input: str = ""
        self.text = ""

        self.root = ctk.CTk()

        self.root.title("ChatBotApp.py")
        self.root.geometry("1280x720")

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure((0, 1, 2), weight=1)

        self.widgets()

        self.input_process()

        self.root.mainloop()

    def widgets(self):

        self.sidebar_frame = ctk.CTkFrame(self.root, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ApoGPT 2.0", font=ctk.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.entry = ctk.CTkEntry(self.root, placeholder_text="Type here...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = ctk.CTkButton(self.root, fg_color="transparent", border_width=2, text="Submit" , text_color=("gray10", "#DCE4EE"), command=self.input_process)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        self.text_label = ctk.CTkLabel(self.root, text=self.text, font=ctk.CTkFont(size=14, weight="bold"))
        self.text_label.grid(row=0, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


    def load_memory(self):
        try:
            with open(self.file_path, "r") as f:
                self.data = json.load(f)
            return self.data
        except FileNotFoundError:
            messagebox.showerror("Error", "An error occurred! Could\'t find \"memory.json\"")

    def save_memory(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.data, f, indent=2)
        except:
            messagebox.showerror("Error", "An error occurred! Could\'t save memory.")
            

    def best_matches(self):
        self.matches = gcm(self.user_input, self.questions, n=1, cutoff=0.6)
        return self.matches[0] if self.matches else None


    def get_ans_4_question(self):
        for i in self.memory["questions"]:
            if i["question"] == self.best_match:
                return i["answer"]


    def input_process(self):
        self.text = "Bot: Hey,There! You can ask me any thing or teach me something new.\n"
        self.user_input = self.entry.get()    
        self.best_match = self.best_matches()

        if self.best_match:
            self.answer = self.get_ans_4_question()
            self.text += f"Bot: {self.answer}\n"

        elif self.user_input: 
            self.text += "Bot: I don\'t know the answer. Can you teach me? if yes please provide a correct answer and don\'t use extra words.\nType the answer or 'skip' to skip.\n"
            self.text_label.after(20000, self.wait_for_answer)

        self.text_label.configure(text=self.text)
        self.entry.delete(0, tk.END)


    def wait_for_answer(self):
        self.new_answer = self.entry.get()

        if self.new_answer.lower() != 'skip':
            self.memory["questions"].append({"question": self.user_input, "answer": self.new_answer})
            self.save_memory()
            self.text += "Bot: Thanks for teaching me!\n"
        else:
            self.text += "Bot: You've chosen to skip teaching. If you want to teach later, just type your question again.\n"

        self.text_label.configure(text=self.text)
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    ChatBotApp()