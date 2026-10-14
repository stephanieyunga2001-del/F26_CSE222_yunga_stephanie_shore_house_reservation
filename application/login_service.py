from data.account_storage import load_accounts
from application.password_utils import verify_password


def login_user(username, password):
    """Verify a user's login credentials."""

    # Check if the username or password is empty
    username = username.strip()

    if not username or not password:
        return False, "Please enter a username and password."

    # Load existing accounts from storage
    try:
        accounts = load_accounts()
    except Exception:
        return False, "Unable to load account information."

    # Check if the username exists
    for name, saved_password in accounts.items():
        if name.lower() == username.lower():

            # Verify the password against its stored hash
            if verify_password(password, saved_password):
                return True, "Login successful."

            return False, "Invalid username or password."

    # Display a generic error if the username does not exist
    return False, "Invalid username or password."
