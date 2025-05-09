from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


class PasswordValidator:
    def __init__(self):
        # Create main window
        self.window = Tk()
        self.window.title("Password Validator")
        self.window.geometry("450x600")

        # Set color scheme
        self.colors = {
            'bg': '#96c8a2',  # Dark background
            'fg': '#000F5C',  # Light text
            'accent': '#fffff4',  # Accent color
            'error': '#BF616A',  # Error red
            'success': '#A3BE8C',  # Success green
            'input_bg': '#fffff4'  # Input background
        }

        # Configure main window background
        self.window.configure(bg=self.colors['bg'])

        # Create and style main frame
        self.main_frame = Frame(self.window, bg=self.colors['bg'], pady=30, padx=40)
        self.main_frame.pack(expand=True, fill='both')

        # Title with custom styling
        title_label = Label(self.main_frame,
                            text="Password Validator",
                            font=('Helvetica', 24, 'bold'),
                            bg=self.colors['bg'],
                            fg=self.colors['accent'])
        title_label.pack(pady=(0, 20))

        # Password entry section
        password_frame = Frame(self.main_frame, bg=self.colors['bg'])
        password_frame.pack(fill='x', pady=10)

        Label(password_frame,
              text="Enter password:",
              font=('Helvetica', 12),
              bg=self.colors['bg'],
              fg=self.colors['fg']).pack(anchor='w')

        # Styled password entry
        self.password_entry = Entry(password_frame,
                                    font=('Helvetica', 12),
                                    show="•",
                                    bg=self.colors['input_bg'],
                                    fg=self.colors['fg'],
                                    insertbackground=self.colors['fg'],
                                    relief='flat',
                                    width=30)
        self.password_entry.pack(pady=10, ipady=5)

        # Show/Hide password toggle with custom styling
        self.show_password = BooleanVar()
        show_pwd_check = Checkbutton(password_frame,
                                     text="Show password",
                                     variable=self.show_password,
                                     command=self.toggle_password_visibility,
                                     bg=self.colors['bg'],
                                     fg=self.colors['fg'],
                                     selectcolor=self.colors['input_bg'],
                                     activebackground=self.colors['bg'],
                                     activeforeground=self.colors['accent'])
        show_pwd_check.pack(anchor='w')

        # Styled validate button
        validate_button = Button(self.main_frame,
                                 text="Validate Password",
                                 command=self.validate_password,
                                 font=('Helvetica', 12, 'bold'),
                                 bg=self.colors['accent'],
                                 fg=self.colors['bg'],
                                 activebackground=self.colors['bg'],
                                 activeforeground=self.colors['accent'],
                                 relief='flat',
                                 padx=20,
                                 pady=10)
        validate_button.pack(pady=20)

        # Result label with custom styling
        self.result_label = Label(self.main_frame,
                                  text="",
                                  wraplength=350,
                                  font=('Helvetica', 11),
                                  bg=self.colors['bg'],
                                  fg=self.colors['fg'])
        self.result_label.pack(pady=10)

        # Requirements section
        req_frame = Frame(self.main_frame, bg=self.colors['bg'])
        req_frame.pack(fill='x', pady=20)

        Label(req_frame,
              text="Password Requirements",
              font=('Helvetica', 14, 'bold'),
              bg=self.colors['bg'],
              fg=self.colors['accent']).pack(anchor='w')

        reqs = [
            "• Minimum 8 characters long",
            "• At least one digit",
            "• Both uppercase and lowercase letters",
            "• Must not contain 'password'",
            "• Cannot start with number or space"
        ]

        for req in reqs:
            Label(req_frame,
                  text=req,
                  font=('Helvetica', 11),
                  bg=self.colors['bg'],
                  fg=self.colors['fg'],
                  anchor='w').pack(fill='x', pady=3)

    def toggle_password_visibility(self):
        self.password_entry.config(show="" if self.show_password.get() else "•")

    def validate_password(self):
        password = self.password_entry.get().strip()

        # Validation checks
        if len(password) < 8:
            self.show_error("Password must be at least 8 characters long.")
            return

        if not any(char.isdigit() for char in password):
            self.show_error("Password must contain at least one digit.")
            return

        if not (any(char.isupper() for char in password) and
                any(char.islower() for char in password)):
            self.show_error("Password must contain both uppercase and lowercase letters.")
            return

        if "password" in password.lower():
            self.show_error("Password must not contain the word 'password'.")
            return

        if password[0].isdigit() or password[0].isspace():
            self.show_error("Password must not start with a number or space.")
            return

        self.result_label.config(text="Password accepted!", fg=self.colors['success'])
        messagebox.showinfo("Success", "Password meets all requirements!")

    def show_error(self, message):
        self.result_label.config(text=message, fg=self.colors['error'])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = PasswordValidator()
    app.run()