import tkinter as tk
from tkinter import ttk

class ShoreHouseApp:
    def __init__(self):
        # Create the main application window
        self.main_win = tk.Tk()

        # Set the window title and minimum size
        self.main_win.title("Bay Shore Get-Away")
        self.main_win.minsize(width=640, height=520)
        self.main_win.configure(bg="#F0F0F0")  # Windows native light gray background

        # --- Title Header ---
        self.title_label = tk.Label(
            self.main_win, 
            text="Shore House Reservation System", 
            font=("Arial", 18), 
            bg="#F0F0F0",
            fg="#000000"
        )
        self.title_label.pack(pady=(35, 20))

        # --- Main Layout Container ---
        self.content_frame = tk.Frame(self.main_win, bg="#F0F0F0")
        self.content_frame.pack(fill="x", padx=40)

        # Left Side: Dedicated frame containing your native PhotoImage asset
        self.image_spacer = tk.Frame(self.content_frame, width=310, height=260, bg="#F0F0F0")
        self.image_spacer.pack(side="left")
        self.image_spacer.pack_propagate(False) # Prevents the frame from shrinking down

        # Load the image to be displayed in the window using native tk.PhotoImage
        # Note: Native PhotoImage natively supports PNG files (not JPG)
        self.photo = tk.PhotoImage(file="gui/shorehouse_image.png")

        # Create and display the image label nested into the layout spacer frame
        self.image_label = tk.Label(
            self.image_spacer,
            image=self.photo,
            bd=0
        )
        self.image_label.pack(fill="both", expand=True)

        # Right Side: Interactive Controls Frame
        self.interactive_frame = tk.Frame(self.content_frame, bg="#F0F0F0")
        self.interactive_frame.pack(side="right", fill="both", expand=True)

        # "Select the Week" Label
        self.select_label = tk.Label(
            self.interactive_frame, 
            text="Select the Week", 
            font=("Arial", 11), 
            bg="#F0F0F0"
        )
        self.select_label.pack(anchor="e", padx=(0, 10), pady=(30, 5))

        # Native Stylized Combobox Dropdown Element
        self.dropdown_var = tk.StringVar()
        self.week_dropdown = ttk.Combobox(
            self.interactive_frame, 
            textvariable=self.dropdown_var, 
            state="readonly", 
            width=20, 
            font=("Arial", 9)
        )
        self.week_dropdown['values'] = ("Select Week",) 
        self.week_dropdown.current(0)
        self.week_dropdown.pack(anchor="e", padx=(0, 10), pady=(0, 100))

        # "Reserve" Action Button
        self.reserve_btn = tk.Button(
            self.interactive_frame, 
            text="Reserve", 
            font=("Arial", 9), 
            width=16, 
            bg="#E1E1E1", 
            fg="#8E8E8E",  
            relief="groove", 
            bd=1,
            state="disabled"
        )
        self.reserve_btn.pack(anchor="e", side="bottom", padx=(0, 10), pady=(0, 10))

        # --- Bottom Section: Pure Text Matrix Data Table ---
        self.table_container = tk.Frame(self.main_win, bg="white")
        self.table_container.pack(fill="x", padx=40, pady=(25, 20))

        # Uniform grid setup to enforce perfectly aligned cell spaces
        self.table_grid = tk.Frame(self.table_container, bg="white")
        self.table_grid.pack(fill="x", padx=10, pady=10)

        self.headers = ["Unit", "Sleeps", "Bdrms", "Bth", "Kitchenette", "Price", "Deposit"]

        # Defining precise column alignments
        self.alignments = ["w", "center", "center", "center", "center", "e", "e"]

        # Setup column expansion constraints to mirror the screenshot proportions
        self.table_grid.columnconfigure(0, weight=3) # Unit gets the most width space
        for col_idx in range(1, 7):
            self.table_grid.columnconfigure(col_idx, weight=1)

        # Render Table Header Row
        for col_idx, head_text in enumerate(self.headers):
            sticky_dir = "w" if self.alignments[col_idx] == "w" else ("e" if self.alignments[col_idx] == "e" else "")
            
            lbl = tk.Label(
                self.table_grid, 
                text=head_text, 
                font=("Arial", 9, "bold"), 
                bg="white", 
                anchor=self.alignments[col_idx]
            )
            
            if head_text == "Bdrms":
                lbl.config(underline=0)
                
            lbl.grid(row=0, column=col_idx, sticky=sticky_dir + "ns", pady=(0, 4))

        # --- Start Main Application Event Loop ---
        self.main_win.mainloop()

# Instantiates and executes the application
if __name__ == "__main__":
    app = ShoreHouseApp()
