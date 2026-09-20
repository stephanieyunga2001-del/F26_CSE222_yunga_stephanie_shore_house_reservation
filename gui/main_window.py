import tkinter as tk


class MainWindow:
    pass


class MainGui:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title("Bay Shore Get-Away")
        self.main_win.minsize(width=550, height=200)

        self.photo = tk.PhotoImage(file="shorepicture.png")

        self.image_label = tk.Label(
            self.main_win,
            image=self.photo
        )
        self.image_label.pack(pady=20)

        self.button_frame = tk.Frame(self.main_win)
        self.button_frame.pack(pady=10)

        self.login_button = tk.Button(
            self.button_frame,
            text="User Login"
        )
        self.login_button.pack(side="left", padx=10)

        self.create_button = tk.Button(
            self.button_frame,
            text="Create Account"
        )
        self.create_button.pack(side="left", padx=10)

        self.quit_button = tk.Button(
            self.button_frame,
            text="Cancel",
            command=self.main_win.destroy
        )
        self.quit_button.pack(side="left", padx=10)

        self.main_win.mainloop()


MainGui()
