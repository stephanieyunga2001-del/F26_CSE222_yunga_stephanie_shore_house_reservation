import tkinter as tk
from gui.login_gui import LoginGui
from gui.account_gui import AccountGUI

class MainWindow:
    pass


class MainGui:
    def __init__(self):
        # Create the main application window
        self.main_win = tk.Tk()

        # Set the window title and minimum size
        self.main_win.title("Bay Shore Get-Away")
        self.main_win.minsize(width=550, height=200)

        # Load the image to be displayed in the window
        self.photo = tk.PhotoImage(file="gui/shorepicture.png")

        # Create and display the image label
        self.image_label = tk.Label(
            self.main_win,
            image=self.photo
        )
        self.image_label.pack(pady=20)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.main_win)
        self.button_frame.pack(pady=10)

        # Create the User Login button
        self.login_button = tk.Button(
            self.button_frame,
            text="User Login",
            command=self.open_login
        )
        self.login_button.pack(side="left", padx=10)

        # Create the Create Account button
        self.create_button = tk.Button(
            self.button_frame,
            text="Create Account",
            command=self.open_account
        )
        self.create_button.pack(side="left", padx=10)

        # Create the Cancel button and close the window when clicked
        self.quit_button = tk.Button(
            self.button_frame,
            text="Cancel",
            command=self.main_win.destroy
        )
        self.quit_button.pack(side="left", padx=10)

        # Start the GUI event loop
        self.main_win.mainloop()

    def open_login(self):
        self.main_win.withdraw()
        LoginGui(self.main_win)

    def open_account(self):
        self.main_win.withdraw()
        AccountGUI(self.main_win)


# Create an instance of the GUI and launch the application
MainGui()
