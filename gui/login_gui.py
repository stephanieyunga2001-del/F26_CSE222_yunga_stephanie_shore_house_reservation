import tkinter as tk
from tkinter import messagebox


class LoginGui:

    def __init__(self, main_win):
        # Keep a reference to the original main window
        self.parent = main_win

        # Create a separate login window
        self.main_win = tk.Toplevel(self.parent)
        self.main_win.title("Bay Shore Get-Away - Login")
        self.main_win.minsize(width=450, height=350)

        # Configure rows and columns
        self.main_win.rowconfigure(0, weight=0)
        self.main_win.rowconfigure(1, weight=0)
        self.main_win.rowconfigure(2, weight=0)
        self.main_win.columnconfigure(0, weight=1)

        # Main image for GUI
        self.photo = tk.PhotoImage(file="loginpicture.png")
        self.labelGIF = tk.Label(self.main_win, image=self.photo)
        self.labelGIF.grid(row=0, column=0, pady=(15, 5))

        # Frame for entry fields
        self.entry_frame = tk.Frame(self.main_win)
        self.entry_frame.grid(row=1, column=0, pady=5)

        # Username label
        self.username_label = tk.Label(
            self.entry_frame, text="User Name:", font=("Arial", 11)
        )
        self.username_label.grid(
            row=0, column=0, sticky="e", padx=5, pady=4
        )

        # Username entry
        self.username_entry = tk.Entry(
            self.entry_frame, width=25, font=("Arial", 11)
        )
        self.username_entry.grid(
            row=0, column=1, padx=5, pady=4
        )

        # Password label
        self.password_label = tk.Label(
            self.entry_frame, text="Password:", font=("Arial", 11)
        )
        self.password_label.grid(
            row=1, column=0, sticky="e", padx=5, pady=4
        )

        # Password entry
        self.password_entry = tk.Entry(
            self.entry_frame, width=25, font=("Arial", 11), show="*"
        )
        self.password_entry.grid(
            row=1, column=1, padx=5, pady=4
        )

        # Instruction label
        self.instruction_label = tk.Label(
            self.main_win,
            text="Enter a username and password and press <enter>",
            font=("Arial", 11),
        )
        self.instruction_label.grid(
            row=2, column=0, pady=(15, 15)
        )

        # Bind Enter to the login function
        self.password_entry.bind("<Return>", self.login_user)

        # Restore the original window when X is clicked
        self.main_win.protocol(
            "WM_DELETE_WINDOW", self.close_window
        )

    def close_window(self):
        self.main_win.destroy()
        self.parent.deiconify()

    def login_user(self, event=None):
        pass




# Create an instance
if __name__ == "__main__":
    loginSystem = LoginGui()
