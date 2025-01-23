import re
import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordSecurityChecker:
    def __init__(self):
        # Creating the main window
        self.window = tk.Tk()
        self.window.title("Password Security Checker")
        self.window.geometry("350x400")
        self.window.configure(bg="#f0f0f0")  # Set background color

        # Create a main frame
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # Creating the input label and area
        input_label = ttk.Label(main_frame, text="Please Enter Your Password:", font=("Cambria", 18))
        input_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        self.input_area = ttk.Entry(main_frame, font=("Cambria", 15), justify="center", show="*")
        self.input_area.grid(row=1, column=0, columnspan=3, padx=(0, 10), sticky=(tk.W, tk.E))

        # Hide and Show button
        self.toggle_button = ttk.Button(main_frame, text="Show", command=self.toggle_password)
        self.toggle_button.grid(row=1, column=3, padx=(10, 0), pady=10)

        # Check button
        self.check_button = ttk.Button(main_frame, text="CHECK", command=lambda: self.pass_checker(self.get_entry()))
        self.check_button.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E), columnspan=4)

        # Safety level
        safety_label1 = ttk.Label(main_frame, text="Your Password Safety Level is:", font=("Cambria", 15))
        safety_label1.grid(row=3, column=0, pady=(15, 5), sticky=tk.W, columnspan=4)

        self.safety_display = ttk.Entry(main_frame, font=("Cambria", 15), justify="center")
        self.safety_display.grid(row=4, column=0, pady=5, sticky="ew", columnspan=4)

        # Password suggestion button
        suggest_button = ttk.Button(main_frame, text="Suggest Password", command=self.pass_suggest)
        suggest_button.grid(row=5, column=0, pady=10, sticky=(tk.W, tk.E), columnspan=2)

        # Clipboard button
        clipboard_button = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_clipboard)
        clipboard_button.grid(row=5, column=2, pady=10, sticky=(tk.W, tk.E), columnspan=2)

        # Start the main loop
        self.window.mainloop()

    def toggle_password(self):
        """Toggle the visibility of the password."""
        if self.input_area.cget('show') == '*':
            self.input_area.config(show='')  # Show password
            self.toggle_button.config(text='Hide')  # Change button text to Hide
        else:
            self.input_area.config(show='*')  # Hide password
            self.toggle_button.config(text='Show')  # Change button text to Show

    def get_entry(self):
        # This is the entry for the password
        password = str(self.input_area.get())
        return password

    def pass_checker(self, password):
        # This function checks the password and gives strength back
        lower, upper, digit, punc = 0, 0, 0, 0
        password_strength = 0
        pass_length = len(password)
        
        if pass_length < 8:
            self.safety_display.delete(0, tk.END)
            self.safety_display.insert(0, "Your password must be at least 8 characters")
            return
        
        try: 
            if 8 <= pass_length < 12:
                password_strength += 0.5
            elif pass_length >= 12:
                password_strength += 1
            
            for ch in password:
                if ch.islower():
                    lower += 1
                if ch.isupper():
                    upper += 1
                if ch.isdigit():
                    digit += 1
                    password_strength += 1
                if ch in string.punctuation:
                    punc += 1
                    password_strength += 1
            
            if not (lower >= 1 and upper >= 1 and digit >= 1 and punc >= 1 and lower + upper + digit + punc == len(password)):
                raise ValueError("Invalid Password")
            
            if password_strength >= 3:
                password_security = "Strong"
            elif password_strength >= 2:
                password_security = "Moderate"
            else:
                password_security = "Weak"

            self.safety_display.delete(0, tk.END)
            self.safety_display.insert(0, password_security)
        
        except ValueError as error:
            self.safety_display.delete(0, tk.END)
            self.safety_display.insert(0, str(error))

    def pass_suggest(self):
        # Generate a strong password suggestion
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        suggested_password = ''.join(random.choice(characters) for i in range(length))
        self.input_area.delete(0, tk.END)
        self.input_area.insert(0, suggested_password)

    def copy_clipboard(self):
        # Copy the suggested password to the clipboard
        suggested_password = self.input_area.get()
        self.window.clipboard_clear()
        self.window.clipboard_append(suggested_password)
        self.window.update()  # Now it stays in clipboard after the window is closed

if __name__ == "__main__":
    app = PasswordSecurityChecker()
