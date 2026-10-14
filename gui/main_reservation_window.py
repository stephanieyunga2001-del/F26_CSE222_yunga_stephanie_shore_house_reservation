import tkinter as tk
from tkinter import ttk

# --- Root Window Setup ---
root = tk.Tk()
root.title("Shore House Reservation System")
root.geometry("640x520")
root.configure(bg="#F0F0F0")  # Windows native light gray background

# --- Title Header ---
title_label = tk.Label(
    root, 
    text="Shore House Reservation System", 
    font=("Arial", 18), 
    bg="#F0F0F0",
    fg="#000000"
)
title_label.pack(pady=(35, 20))

# --- Main Layout Container ---
content_frame = tk.Frame(root, bg="#F0F0F0")
content_frame.pack(fill="x", padx=40)

# Left Side: Empty Frame acting as a rigid layout spacer matching the photo's footprint
image_spacer = tk.Frame(content_frame, width=310, height=260, bg="#F0F0F0")
image_spacer.pack(side="left")
image_spacer.pack_propagate(False) # Prevents the frame from shrinking down

# Right Side: Interactive Controls Frame
interactive_frame = tk.Frame(content_frame, bg="#F0F0F0")
interactive_frame.pack(side="right", fill="both", expand=True)

# "Select the Week" Label
select_label = tk.Label(
    interactive_frame, 
    text="Select the Week", 
    font=("Arial", 11), 
    bg="#F0F0F0"
)
select_label.pack(anchor="e", padx=(0, 10), pady=(30, 5))

# Native Stylized Combobox Dropdown Element
dropdown_var = tk.StringVar()
week_dropdown = ttk.Combobox(
    interactive_frame, 
    textvariable=dropdown_var, 
    state="readonly", 
    width=20, 
    font=("Arial", 9)
)
week_dropdown['values'] = ("Select Week",) # Removed "Week 1", "Week 2", "Week 3"
week_dropdown.current(0)
week_dropdown.pack(anchor="e", padx=(0, 10), pady=(0, 100))

# "Reserve" Action Button
# Styled matching the grayed-out appearance in the mockup image
reserve_btn = tk.Button(
    interactive_frame, 
    text="Reserve", 
    font=("Arial", 9), 
    width=16, 
    bg="#E1E1E1", 
    fg="#8E8E8E",  
    relief="groove", 
    bd=1,
    state="disabled"
)
reserve_btn.pack(anchor="e", side="bottom", padx=(0, 10), pady=(0, 10))


# --- Bottom Section: Pure Text Matrix Data Table ---
# Structured container framing the white text data block
table_container = tk.Frame(root, bg="white")
table_container.pack(fill="x", padx=40, pady=(25, 20))

# Uniform grid setup to enforce perfectly aligned cell spaces
table_grid = tk.Frame(table_container, bg="white")
table_grid.pack(fill="x", padx=10, pady=10)

headers = ["Unit", "Sleeps", "Bdrms", "Bth", "Kitchenette", "Price", "Deposit"]

# Defining precise column alignments
# Text descriptions align left ('w'), numeric amounts align right ('e'), metrics center
alignments = ["w", "center", "center", "center", "center", "e", "e"]

# Setup column expansion constraints to mirror the screenshot proportions
table_grid.columnconfigure(0, weight=3) # Unit gets the most width space
for col_idx in range(1, 7):
    table_grid.columnconfigure(col_idx, weight=1)

# Render Table Header Row
for col_idx, head_text in enumerate(headers):
    sticky_dir = "w" if alignments[col_idx] == "w" else ("e" if alignments[col_idx] == "e" else "")
    
    lbl = tk.Label(
        table_grid, 
        text=head_text, 
        font=("Arial", 9, "bold"), 
        bg="white", 
        anchor=alignments[col_idx]
    )
    
    # Replicates the spelling warning line under "Bdrms" seen in the image
    if head_text == "Bdrms":
        lbl.config(underline=0)
        
    lbl.grid(row=0, column=col_idx, sticky=sticky_dir + "ns", pady=(0, 4))

# Removed the data rows section completely to leave only the headers

# --- Start Main Application Event Loop ---
root.mainloop()
