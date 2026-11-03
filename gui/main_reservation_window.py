import tkinter as tk
from tkinter import ttk
from data.unit_storage import load_units


class ShoreHouseApp:

    def __init__(self, main_win):

        # Use the existing main application window
        self.main_win = main_win

        # Set the window title and minimum size
        self.main_win.title("Bay Shore Get-Away")
        self.main_win.minsize(width=640, height=520)
        self.main_win.configure(bg="#F0F0F0")

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
        self.content_frame = tk.Frame(
            self.main_win,
            bg="#F0F0F0"
        )
        self.content_frame.pack(fill="x", padx=40)

        # Left Side: Photo Frame
        self.image_spacer = tk.Frame(
            self.content_frame,
            width=310,
            height=260,
            bg="#F0F0F0"
        )
        self.image_spacer.pack(side="left")
        self.image_spacer.pack_propagate(False)

        # Load image
        raw_photo = tk.PhotoImage(
            file="gui/shorehouse_image.png"
        )

        self.main_win.shore_photo = raw_photo.subsample(2, 2)

        self.image_label = tk.Label(
            self.image_spacer,
            image=self.main_win.shore_photo,
            bd=0
        )
        self.image_label.pack(fill="both", expand=True)

        # Right Side: Interactive Controls
        self.interactive_frame = tk.Frame(
            self.content_frame,
            bg="#F0F0F0"
        )
        self.interactive_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Select the Week Label
        self.select_label = tk.Label(
            self.interactive_frame,
            text="Select the Week",
            font=("Arial", 11),
            bg="#F0F0F0"
        )
        self.select_label.pack(
            anchor="e",
            padx=(0, 10),
            pady=(30, 5)
        )

        # Week Dropdown
        self.dropdown_var = tk.StringVar()

        self.week_dropdown = ttk.Combobox(
            self.interactive_frame,
            textvariable=self.dropdown_var,
            state="readonly",
            width=20,
            font=("Arial", 9)
        )

        self.week_dropdown["values"] = ("Select Week",)
        self.week_dropdown.current(0)

        self.week_dropdown.pack(
            anchor="e",
            padx=(0, 10),
            pady=(0, 100)
        )

        # Reserve Button
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

        self.reserve_btn.pack(
            anchor="e",
            side="bottom",
            padx=(0, 10),
            pady=(0, 10)
        )

        # Rental Information Table
        self.table_container = tk.Frame(
            self.main_win,
            bg="white"
        )
        self.table_container.pack(
            fill="x",
            padx=40,
            pady=(25, 20)
        )

        self.table_grid = tk.Frame(
            self.table_container,
            bg="white"
        )
        self.table_grid.pack(fill="x", padx=10, pady=10)

        # Table Headers
        self.headers = [
            "Unit", "Sleeps", "Bdrms", "Bth",
            "Kitchenette", "Price", "Deposit"
        ]

        # Column Alignments
        self.alignments = [
            "w", "center", "center", "center",
            "center", "e", "e"
        ]

        # Setup column expansion constraints
        self.table_grid.columnconfigure(0, weight=3)

        for col_idx in range(1, 7):
            self.table_grid.columnconfigure(
                col_idx, weight=1
            )

        # Render Table Header Row
        for col_idx, head_text in enumerate(self.headers):

            sticky_dir = (
                "w" if self.alignments[col_idx] == "w"
                else "e" if self.alignments[col_idx] == "e"
                else ""
            )

            lbl = tk.Label(
                self.table_grid,
                text=head_text,
                font=("Arial", 9, "bold"),
                bg="white",
                anchor=self.alignments[col_idx]
            )

            lbl.grid(
                row=0,
                column=col_idx,
                sticky=sticky_dir + "ns",
                pady=(0, 4)
            )

        # Load rental unit data
        self.units = load_units()

        # Display rental information
        for row_idx, unit in enumerate(self.units, start=1):

            # Format bathroom values as number + fraction
            bathrooms = {
                2.5: "2 1/2"
            }
            formatted_unit = [
                unit[0],
                unit[1],
                unit[2],
                bathrooms.get(unit[3], str(unit[3]).rstrip("0").rstrip(".")),
                unit[4],
                f"${unit[5]:,.0f}",
                f"${unit[6]:,.2f}"
            ]

            for col_idx, value in enumerate(formatted_unit):

                sticky_dir = (
                    "w" if self.alignments[col_idx] == "w"
                    else "e" if self.alignments[col_idx] == "e"
                    else ""
                )

                lbl = tk.Label(
                    self.table_grid,
                    text=value,
                    font=("Arial", 9),
                    bg="white",
                    anchor=self.alignments[col_idx]
                )

                lbl.grid(
                    row=row_idx,
                    column=col_idx,
                    sticky=sticky_dir + "ns",
                    pady=4
                )
