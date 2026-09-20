import tkinter as tk  # import the tkinter module
from tkinter import messagebox


class AccountGUI:  # declares class

    def __init__(self):  # initialization function
        self.main_win = tk.Tk()  # main window creation
        self.main_win.title("Account Creation")  # title bar label
        self.main_win.minsize(width=500, height=400)  # window size

        # Row configuration to properly center content
        self.main_win.rowconfigure(0, weight=1)
        self.main_win.rowconfigure(1, weight=1)

        # Column for centered grid placement
        self.main_win.columnconfigure(0, weight=1)

        # Frame that clusters all the username widgets
        self.username_frame = tk.Frame(self.main_win)
        self.username_frame.grid(row=0, column=0, pady=(30, 10))

        # Username entry field instruction label
        self.username_label = tk.Label(
            self.username_frame,
            text="Create a user name",
            font=("Arial", 12)
        )
        self.username_label.pack(pady=(10, 5))

        # Input field for creating a new user name
        self.username_entry = tk.Entry(
            self.username_frame,
            width=25,
            font=("Arial", 11)
        )
        self.username_entry.pack(pady=5)

        # Frame that clusters all the password widgets
        self.password_frame = tk.Frame(self.main_win)
        self.password_frame.grid(row=1, column=0, pady=(10, 30))

        # Text block containing password requirements and enter key instruction
        password_text = (
            "Create a password of at least nine (9) characters,\n"
            "that contains at least one digit, one uppercase,\n"
            "and one lowercase letter. Then press <enter>"
        )

        # Password criteria requirement label
        self.password_label = tk.Label(
            self.password_frame,
            text=password_text,
            font=("Arial", 11),
            justify="center",
        )
        self.password_label.pack(pady=(10, 5))

        # Input field for creating a secure password
        self.password_entry = tk.Entry(
            self.password_frame,
            width=35,
            font=("Arial", 11)
        )
        self.password_entry.pack(pady=5)

        # Binds the entry field to trigger code logic when enter is pressed
        self.password_entry.bind("<Return>", self.submit_account)

        self.main_win.mainloop()  # starts loop to keep window open

    def submit_account(self, event):  # placeholder for enter press trigger
        pass


# Create an instance
if __name__ == "__main__":
    accountGui = AccountGUI()
