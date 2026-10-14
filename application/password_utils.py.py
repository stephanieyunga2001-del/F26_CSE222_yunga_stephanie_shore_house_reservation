import hashlib
import secrets
import hmac


def hash_password(password):
    """Hash a password using a random salt."""

    # Generate a random 16-byte salt
    salt = secrets.token_bytes(16)

    # Hash the password using PBKDF2 and SHA-256
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
    )

    # Return the salt and hash together for storage
    return salt.hex() + ":" + password_hash.hex()


def verify_password(password, stored_password):
    """Verify a password against its stored salted hash."""

    try:
        # Separate the salt and hash
        salt_hex, hash_hex = stored_password.split(":")

        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)

        # Hash the entered password using the original salt
        actual_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            600_000
        )

        # Compare hashes safely
        return hmac.compare_digest(
            actual_hash,
            expected_hash
        )

    except (ValueError, TypeError):
        return False
