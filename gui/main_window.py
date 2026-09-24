import tkinter as tk
from tkinter import messagebox
from account_gui import AccountGUI


class MainWindow:
    def __init__(self):

        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Bay Shore Get-Away")
        self.main_window.minsize(width=550, height=200)

        # Configure columns
        self.main_window.columnconfigure(1, weight=1)
        self.main_window.columnconfigure(2, weight=1)
        self.main_window.columnconfigure(3, weight=1)
        self.main_window.columnconfigure(4, weight=1)
        self.main_window.columnconfigure(5, weight=1)

        # Create the heading frame
        self.heading_frame = tk.Frame(
            width=80,
            height=50
        )
        self.heading_frame.grid(
            row=1,
            column=1,
            columnspan=5
        )

        # Create the heading label
        self.heading_label = tk.Label(
            text="Bay Shore Get-Away",
            font=("Helvetica", 16),
            fg="blue"
        )
        self.heading_label.grid(
            row=2,
            column=2,
            columnspan=3,
            rowspan=2,
            padx=15,
            pady=15
        )

        # Get the beach image
        photo = tk.PhotoImage(
            file="Beach.png"
        )

        # Create the image label
        self.labelPNG = tk.Label(
            image=photo
        )

        # Retain a reference to the image
        self.labelPNG.image = photo

        # Position the beach image
        self.labelPNG.grid(
            row=5,
            column=1,
            columnspan=5,
            padx=15,
            pady=15
        )

        # Create the User Login button
        self.login_button = tk.Button(
            text=" User Login ",
            width=16,
            font=("Helvetica", 10)
        )
        self.login_button.grid(
            row=6,
            column=1,
            padx=10,
            pady=15
        )

        # Create the Create Account button
        self.create_acct_button = tk.Button(
            text=" Create Account ",
            width=18,
            font=("Helvetica", 10),
            command=self.open_account
        )
        self.create_acct_button.grid(
            row=6,
            column=3,
            padx=10,
            pady=15
        )

        # Create the Cancel button
        self.quit_button = tk.Button(
            text=" Cancel ",
            width=16,
            font=("Helvetica", 10),
            command=self.main_window.destroy
        )
        self.quit_button.grid(
            row=6,
            column=5,
            padx=10,
            pady=15
        )

                # Enter the tkinter main loop
        tk.mainloop()

    # Open the Account Creation window
    def open_account(self):
        AccountGUI()


# Create an instance of the class
shoreHouse = MainWindow()
