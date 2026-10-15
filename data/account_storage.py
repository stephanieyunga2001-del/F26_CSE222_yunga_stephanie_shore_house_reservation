import json
import os

# Defines the location of the account storage JSON file
ACCOUNT_FILE = os.path.join(
    os.path.dirname(__file__),
    "accounts.json"
)

# Checks if the file exists for error checking
def load_accounts():
    if not os.path.exists(ACCOUNT_FILE):
        return {}
        
# Opens the JSON file in read mode and converts the data into Python data
# Catches invalid JSON format errors and file system errors preventing read access
    try:
        with open(ACCOUNT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}

# Saves account data into the json file by opening the file in write mode
def save_accounts(accounts):
    try:
        with open(ACCOUNT_FILE, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)
        return True
    except OSError:
        return False

# Searches the JSON file for an account and returns its data if found
def get_account(username):
    accounts = load_accounts()

    for saved_username, account_data in accounts.items():
        if saved_username.lower() == username.strip().lower():
            return account_data

    return None
