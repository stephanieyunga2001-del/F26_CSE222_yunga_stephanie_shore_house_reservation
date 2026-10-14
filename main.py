import tkinter as tk
from gui.main_window import MainWindow

if __name__ == "__main__":
    # 1. Create the single, root application window
    root = tk.Tk()
    
    # 2. Initialize your main window class with the root
    app = MainWindow(root)
    
    # 3. Start the application loop
    root.mainloop()
