from jose import JWTError, jwt
from datetime import datetime, timedelta

# Secret key (we'll move this to .env later)
SECRET_KEY = "vaultx_super_secret_key"

# Algorithm used to sign the token
ALGORITHM = "HS256"

# Token expiry time
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt