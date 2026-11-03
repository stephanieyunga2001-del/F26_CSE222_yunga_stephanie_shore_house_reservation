import tkinter as tk
from tkinter import ttk
from data.unit_storage import load_units
from application.reservation_service import get_available_units
from application.reservation_service import check_reservation
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import date, timedelta

class ShoreHouseApp:

    # Open the rental calendar
    def open_calendar(self):
        calendar_window = tk.Toplevel(self.main_win)
        calendar_window.title("2027 Rental Calendar")
        calendar_window.geometry("350x350")

        calendar = Calendar(
            calendar_window,
            selectmode="day",
            year=2027,
            month=5,
            day=23,
            date_pattern="mm/dd/yyyy",
            weekenddays=[6, 7],
            showweeknumbers=False
        )

        calendar.pack(pady=20)
        calendar.selection_clear()
        
        # Select a rental week from the calendar
        def select_rental_week(event):
            selected_date = calendar.selection_get()

            # Start reservation on the clicked date
            self.selected_start = selected_date

            # End reservation 7 days later
            self.selected_end = selected_date + timedelta(days=7)

            # Display selected dates
            self.selected_week_label.config(
                text=(
                    f"{self.selected_start:%m/%d/%Y} - "
                    f"{self.selected_end:%m/%d/%Y}"
                )
            )

            # Close the calendar
            calendar_window.destroy()
        calendar.bind("<<CalendarSelected>>", select_rental_week)

           # Logic for reserving rooms
    def reserve_unit(self):

        # Check whether reservation dates were selected
        if self.selected_start is None:
            messagebox.showwarning(
                "Missing Selection",
                "Please select a reservation date from the calendar."
            )
            return

        # Get the selected reservation dates
        selected_week = (
            f"{self.selected_start:%m/%d/%Y} - "
            f"{self.selected_end:%m/%d/%Y}"
        )

        

        selected_unit = self.unit_var.get()

        success, message = check_reservation(
            selected_unit,
            selected_week
        )

        # Displays message on success of a reservation
        if success:
            tk.messagebox.showinfo(
                "Reservation",
                f"{message}\n\n"
                f"Unit: {selected_unit}\n"
                f"Week: {selected_week}"
            )

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
            text="Select Your Reservation Date",
            font=("Arial", 11),
            bg="#F0F0F0"
        )
        self.select_label.pack(
            anchor="e",
            padx=(0, 10),
            pady=(30, 5)
        )

        #Store reservation dates
        self.selected_start = None
        self.selected_end = None

        # Display selected reservation dates
        self.selected_week_label = tk.Label(
            self.interactive_frame,
            text="No reservation dates selected",
            font=("Arial", 10),
            bg="#F0F0F0"
        )

        self.selected_week_label.pack(
            anchor="e",
            padx=(0, 10),
            pady=(10, 20)
        )
        # Calendar Button
        self.calendar_button = tk.Button(
        self.interactive_frame,
        text="Open Calendar",
        font=("Arial", 9),
        command=self.open_calendar
    )

        self.calendar_button.pack(
        anchor="e",
        padx=(0, 10),
        pady=(0, 10)
    )

        # Reserve Button
        self.reserve_btn = tk.Button(
            self.interactive_frame,
            text="Reserve",
            font=("Arial", 9),
            width=16,
            bg="#228B22",
            fg="white",
            relief="groove",
            bd=1,
            state="normal",
            command=self.reserve_unit
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
        # Store the selected rental unit
        self.unit_var = tk.StringVar(value="Ground Floor")
        # Floor selection buttons
        self.floor_frame = tk.Frame(
            self.main_win,
            bg="#F0F0F0"
        )

        self.floor_frame.pack(pady=10)

        for unit in self.units:
            tk.Radiobutton(
                self.floor_frame,
                text=unit[0],
                variable=self.unit_var,
                value=unit[0],
                font=("Arial", 10),
                bg="#F0F0F0"
            ).pack(side="left", padx=10)

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
