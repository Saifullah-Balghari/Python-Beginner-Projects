import customtkinter as ctk
from difflib import get_close_matches as gcm
import tkinter as tk
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ChatBotApp:
    def __init__(self):

        # Variable declarations
        self.icon_path = 'logo.png'
        self.file_path  = 'memory.json'
        self.memory: dict = self.load_memory()
        self.questions: list | None = [ i ['question'] for i in self.memory['questions']]
        self.user_input: str = ""
        self.text = ""

        # Making an instance of CustomTKinter
        self.root = ctk.CTk()

        # Basic Configurations
        self.root.title("ChatBotApp.py")
        self.root.geometry("1280x720")
        self.root.iconbitmap(self.icon_path)

        # Grid Configurations
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure((0, 1, 2), weight=1)

        # Calling the main widgets method
        self.widgets()

        # Calling the main method
        self.input_process()

        # Running the main GUI
        self.root.mainloop()

    def widgets(self):

        # Side bar frame
        self.sidebar_frame = ctk.CTkFrame(self.root, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        # logo
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ApoGPT 2.0", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Appearance mode option menu
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # Scaling option menu
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Main entry box and button
        self.entry = ctk.CTkEntry(self.root, placeholder_text=" Type here...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.main_button_1 = ctk.CTkButton(self.root, fg_color="transparent", border_width=2, text="Submit" , text_color=("gray10", "#DCE4EE"), command=self.input_process)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # Main text label
        self.text_label = ctk.CTkLabel(self.root, text=self.text)
        self.text_label.grid(row=0, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


    def load_memory(self):
        """ Takes a file path as input, reads JSON data from the file,
        and returns it as a dictionary"""
        with open(self.file_path, "r") as f:
            self.data = json.load(f)
        return self.data


    def save_memory(self):
        """ Takes in a file path and a dictionary, and saves the dictionary into a 
        file path(JSON file) with specified indentation"""
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=2)


    def best_matches(self):
        """ Finds the best match with the accuracy of 60%"""
        self.matches = gcm(self.user_input, self.questions, n=1, cutoff=0.6)
        return self.matches[0] if self.matches else None


    def get_ans_4_question(self):
        for i in self.memory["questions"]:
            if i["question"] == self.best_match:
                return i["answer"]


    def input_process(self):
        self.user_input = self.entry.get()
        if self.user_input.lower() == 'quit':
            return None
        else:
            self.best_match = self.best_matches()
            if self.best_match:
                self.answer = self.get_ans_4_question()
                self.text += f"Bot: {self.answer}\n"
            else:
                self.text += "Bot: I don\'t know the answer. Can you teach me? if yes please provide a correct answer and don\'t use extra words.\nType the answer or 'skip' to skip."
                new_answer = self.entry.get()
                if new_answer.lower() != 'skip':
                    self.memory["questions"].append({"question": self.user_input, "answer": new_answer})
                    self.save_memory()
                    self.text += "Thanks for teaching me!\n"
        self.text_label.configure(text=self.text)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    ChatBotApp()

