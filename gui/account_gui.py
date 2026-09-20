import tkinter as tk


class AccountGUI:

    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title("Account Creation")
        self.main_win.minsize(width=500, height=400)

        self.main_win.rowconfigure(0, weight=1)
        self.main_win.rowconfigure(1, weight=1)

        self.main_win.columnconfigure(0, weight=1)

        self.username_frame = tk.Frame(self.main_win)
        self.username_frame.grid(row=0, column=0, pady=(30, 10))

        self.username_label = tk.Label(self.username_frame)
        self.username_label.pack(pady=(10, 5))

        self.username_entry = tk.Entry(self.username_frame, width=25)
        self.username_entry.pack(pady=5)

        self.password_frame = tk.Frame(self.main_win)
        self.password_frame.grid(row=1, column=0, pady=(10, 30))

        self.password_label = tk.Label(self.password_frame)
        self.password_label.pack(pady=(10, 5))

        self.password_entry = tk.Entry(self.password_frame, width=35)
        self.password_entry.pack(pady=5)

        self.main_win.mainloop()


accountGui = AccountGUI()
