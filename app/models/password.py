from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)

    website = Column(String, nullable=False)

    account_username = Column(String, nullable=False)

    encrypted_password = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="passwords")