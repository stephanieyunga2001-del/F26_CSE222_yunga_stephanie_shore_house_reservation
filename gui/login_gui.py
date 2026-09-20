import tkinter as tk


class LoginGui:

    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title("Bay Shore Get-Away")
        self.main_win.minsize(width=450, height=350)

        self.main_win.rowconfigure(0, weight=0)
        self.main_win.rowconfigure(1, weight=0)
        self.main_win.rowconfigure(2, weight=0)

        self.main_win.columnconfigure(0, weight=1)

        self.photo = tk.PhotoImage(file="loginpicture.png")
        self.labelGIF = tk.Label(self.main_win, image=self.photo)
        self.labelGIF.grid(row=0, column=0, pady=(15, 5))

        self.entry_frame = tk.Frame(self.main_win)
        self.entry_frame.grid(row=1, column=0, pady=5)

        self.username_label = tk.Label(self.entry_frame)
        self.username_label.grid(row=0, column=0)

        self.username_entry = tk.Entry(self.entry_frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.entry_frame)
        self.password_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self.entry_frame)
        self.password_entry.grid(row=1, column=1)

        self.instruction_label = tk.Label(self.main_win)
        self.instruction_label.grid(row=2, column=0)

        self.main_win.mainloop()


loginSystem = LoginGui()
