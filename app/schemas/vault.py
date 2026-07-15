from pydantic import BaseModel

class VaultCreate(BaseModel):
    title: str
    website: str
    username: str
    password: str
    category: str


class VaultUpdate(BaseModel):
    title: str
    website: str
    username: str
    password: str
    category: str