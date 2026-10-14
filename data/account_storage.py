import json
import os


ACCOUNT_FILE = os.path.join(
    os.path.dirname(__file__),
    "accounts.json"
)


def load_accounts():
    if not os.path.exists(ACCOUNT_FILE):
        return {}

    try:
        with open(ACCOUNT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_accounts(accounts):
    try:
        with open(ACCOUNT_FILE, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)
        return True
    except OSError:
        return False


def get_account(username):
    accounts = load_accounts()

    for saved_username, account_data in accounts.items():
        if saved_username.lower() == username.strip().lower():
            return account_data

    return None
