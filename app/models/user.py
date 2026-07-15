from sqlalchemy import Column, Integer, String
from app.database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    vaults = relationship("Vault", back_populates="owner")
    vaults = relationship("Vault", back_populates="owner")