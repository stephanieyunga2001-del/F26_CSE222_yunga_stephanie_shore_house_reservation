import tkinter as tk
from tkinter import messagebox
from data.account_storage import load_accounts, save_accounts
from application.account_service import validate_password
from application.password_utils import hash_password


class AccountGUI:

    def __init__(self, main_win):
        # Keep a reference to the original main window
        self.parent = main_win

        # Create a separate account creation window
        self.main_win = tk.Toplevel(self.parent)
        self.main_win.title("Account Creation")
        self.main_win.minsize(width=500, height=400)

        # Row configuration to properly center content
        self.main_win.rowconfigure(0, weight=1)
        self.main_win.rowconfigure(1, weight=1)

        # Column for centered grid placement
        self.main_win.columnconfigure(0, weight=1)

        # Frame that clusters all the username widgets
        self.username_frame = tk.Frame(self.main_win)
        self.username_frame.grid(
            row=0, column=0, pady=(30, 10)
        )

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
        self.password_frame.grid(
            row=1, column=0, pady=(10, 30)
        )

        # Password requirements and Enter instruction
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
            font=("Arial", 11),
            show="*"
        )
        self.password_entry.pack(pady=5)

        # Bind Enter to the account submission function
        self.password_entry.bind(
            "<Return>", self.submit_account
        )

        # Return to the original window when X is clicked
        self.main_win.protocol(
            "WM_DELETE_WINDOW", self.close_window
        )

    def close_window(self):
        # Close the account creation window
        self.main_win.destroy()

        # Return to the original main window
        self.parent.deiconify()

    def submit_account(self, event=None):
        # Get the username and password entered by the user
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        # Check if the username is empty
        if not username:
            messagebox.showerror(
                "Invalid Username",
                "Please enter a username.",
                parent=self.main_win
            )
            self.username_entry.focus_set()
            return

        # Check if the password meets all requirements
        password_error = validate_password(password)

        if password_error:
            # Display an error message if the password is invalid
            messagebox.showerror(
                "Invalid Password",
                password_error,
                parent=self.main_win
            )

            # Clear the password entry field
            self.password_entry.delete(0, tk.END)

            # Return the cursor to the password entry field
            self.password_entry.focus_set()

            # Stop checking the password
            return

        # Load existing accounts from the storage file
        accounts = load_accounts()

        # Check if the username already exists
        if any(name.lower() == username.lower() for name in accounts):
            messagebox.showerror(
                "Username Taken",
                "That username already exists. Please choose another.",
                parent=self.main_win
            )
            self.username_entry.delete(0, tk.END)
            self.username_entry.focus_set()
            return

        # Hashes the password before saving the account
        hashed_password = hash_password(password)

        # Save the username and hashed password
        account[username] = hashed_password
        
        if save_accounts(accounts):
            # Display a confirmation message when the account is saved
            messagebox.showinfo(
                "Account Created",
                "Your account was created successfully!",
                parent=self.main_win
            )

            # Close the account creation window
            self.main_win.destroy()

            # Return to the original main window
            self.parent.deiconify()

        else:
            # Display an error if the account could not be saved
            messagebox.showerror(
                "Save Error",
                "Unable to save account information.",
                parent=self.main_win
            )


# Create an instance
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    accountGui = AccountGUI(root)
    root.mainloop()
