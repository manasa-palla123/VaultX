import re


def check_password_strength(password: str) -> str:
    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Number
    if re.search(r"\d", password):
        score += 1

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"