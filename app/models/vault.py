from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Vault(Base):
    __tablename__ = "vaults"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    username = Column(String, nullable=False)

    password = Column(String, nullable=False)

    website = Column(String)

    category = Column(String, nullable=False)

    
    is_favorite = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="vaults")