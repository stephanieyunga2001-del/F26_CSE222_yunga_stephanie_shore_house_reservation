import tkinter as tk


class AccountGUI:
    def __init__(self):

        # Create the Account Creation window
        self.window = tk.Toplevel()
        self.window.title("Account Creation")
        self.window.minsize(width=400, height=300)

                # Create the heading
        self.heading_label = tk.Label(
            self.window,
            text="Create Account",
            font=("Helvetica", 16),
            fg="blue"
        )

        self.heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=15,
            pady=15
        )

                # Create username instructions
        self.username_label = tk.Label(
            self.window,
            text="Create a user name",
            font=("Helvetica", 10)
        )

        self.username_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

                # Create username entry box
        self.username_entry = tk.Entry(
            self.window,
            width=20
        )

        self.username_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

                # Create password instructions
        self.password_label = tk.Label(
            self.window,
            text="Create a password of at least nine (9) characters,\n"
                 "that contains at least one digit, one uppercase,\n"
                 "and one lowercase letter.",
            font=("Helvetica", 10)
        )

        self.password_label.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=15,
            pady=15
        )

                # Create password entry box
        self.password_entry = tk.Entry(
            self.window,
            width=20,
            show="*"
        )

        self.password_entry.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

                # Create the Create Account button
        self.create_button = tk.Button(
            self.window,
            text=" Create Account ",
            width=18,
            font=("Helvetica", 10)
        )

        self.create_button.grid(
            row=4,
            column=0,
            padx=10,
            pady=15
        )

                # Create the Cancel button
        self.cancel_button = tk.Button(
            self.window,
            text=" Cancel ",
            width=16,
            font=("Helvetica", 10),
            command=self.window.destroy
        )

        self.cancel_button.grid(
            row=4,
            column=1,
            padx=10,
            pady=15
        )

        
        
