import os
import csv

# Locate unit_data.txt inside the data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UNITS_FILE = os.path.join(BASE_DIR, "unit_data.txt")


def load_units():
    """Load rental units from the flat file."""

    units = []

    with open(UNITS_FILE, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            unit = (
                row[0],       # Unit name
                int(row[1]),  # Sleeps
                int(row[2]),  # Bedrooms
                float(row[3]),# Bathrooms
                row[4],       # Kitchenette
                float(row[5]),# Price
                float(row[6]) # Deposit
            )

            units.append(unit)

    return units
