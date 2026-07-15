import bcrypt


def hash_password(password: str) -> str:
    """Convert a plain password into a secure hash."""
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Check if a password matches its stored hash."""
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )