from data.unit_storage import load_units

# Determines what rental units are available
def get_available_units(selected_week):

    units = load_units()

    available_units = []

    for unit in units:
        available_units.append(unit)

    return available_units

# Checks whether a unit is available during a selected week
def check_reservation(unit_name, selected_week):
    """
    Check whether a selected rental unit is available.
    """

# Returns message if unit is available or unavailable
    available_units = get_available_units(selected_week)

    for unit in available_units:
        if unit[0] == unit_name:
            return True, "Unit is available!"

    return False, "Unit is not available."
