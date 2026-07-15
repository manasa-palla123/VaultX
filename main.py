from fastapi import FastAPI
from app.routers.home import router as home_router
from app.auth.auth import router as auth_router
from app.database.database import engine, Base
from app.models.user import User
from app.models.vault import Vault
from app.routers.vault import router as vault_router

app = FastAPI()

app.include_router(home_router)
app.include_router(auth_router)
app.include_router(vault_router)

Base.metadata.create_all(bind=engine)