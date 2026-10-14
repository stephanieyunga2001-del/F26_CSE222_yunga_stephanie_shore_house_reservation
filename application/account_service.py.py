from application.password_utils import hash_password
# Validates password complexity and length requirements
def validate_password(password):
    """Check whether a password meets all requirements."""

    if len(password) < 9:
        return "Password must be at least 9 characters long."

    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    return None
