from cryptography.fernet import Fernet

FERNET_KEY = "KrypLfm6UUOBV-g7avYmyQYPwDrJsCzsAGQOS57ZhM0="

cipher = Fernet(FERNET_KEY.encode())


def encrypt_password(password: str) -> str:
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    return cipher.decrypt(encrypted_password.encode()).decode()