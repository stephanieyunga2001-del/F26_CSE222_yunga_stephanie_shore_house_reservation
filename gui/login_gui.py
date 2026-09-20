import tkinter as tk  # import the tkinter module
from tkinter import messagebox


class LoginGui:  # declares class

    def __init__(self):  # initialization function
        self.main_win = tk.Tk()  # main window creation
        self.main_win.title("Bay Shore Get-Away")  # title bar label
        self.main_win.minsize(width=450, height=350)  # window size

        # Row configuration to stack components tightly
        self.main_win.rowconfigure(0, weight=0)
        self.main_win.rowconfigure(1, weight=0)
        self.main_win.rowconfigure(2, weight=0)

        # Column for centered grid placement
        self.main_win.columnconfigure(0, weight=1)

        # Main image for GUI
        self.photo = tk.PhotoImage(file="loginpicture.png")
        self.labelGIF = tk.Label(self.main_win, image=self.photo)
        self.labelGIF.grid(row=0, column=0, pady=(15, 5))

        # Frame that clusters all the user entry fields together directly below the image
        self.entry_frame = tk.Frame(self.main_win)
        self.entry_frame.grid(row=1, column=0, pady=5)

        # Top row: User Name Label
        self.username_label = tk.Label(
            self.entry_frame, text="User Name:", font=("Arial", 11)
        )
        self.username_label.grid(row=0, column=0, sticky="e", padx=5, pady=4)

        # Top row: User Name entry input box
        self.username_entry = tk.Entry(
            self.entry_frame, width=25, font=("Arial", 11)
        )
        self.username_entry.grid(row=0, column=1, padx=5, pady=4)

        # Bottom row: Password Label
        self.password_label = tk.Label(
            self.entry_frame, text="Password:", font=("Arial", 11)
        )
        self.password_label.grid(row=1, column=0, sticky="e", padx=5, pady=4)

        # Bottom row: Password entry input box with character masking
        self.password_entry = tk.Entry(
            self.entry_frame, width=25, font=("Arial", 11), show="*"
        )
        self.password_entry.grid(row=1, column=1, padx=5, pady=4)

        # Instruction text label positioned closely underneath the input blocks
        self.instruction_label = tk.Label(
            self.main_win,
            text="Enter a username and password and press <enter>",
            font=("Arial", 11),
        )
        self.instruction_label.grid(row=2, column=0, pady=(15, 15))

        # Binds the entry field to trigger code logic when enter is pressed
        self.password_entry.bind("<Return>", self.login_user)

        self.main_win.mainloop()  # starts loop to keep window open

    def login_user(self, event):  # placeholder for enter press trigger
        pass


# Create an instance
loginSystem = LoginGui()
