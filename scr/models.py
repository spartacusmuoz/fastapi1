from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from scr.database import Base
from typing import Optional

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    phone = Column(String(20))
    
    addresses = relationship("Address", back_populates="owner")

class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True,)
    user_id = Column(Integer, ForeignKey("users.id"))
    city = Column(String)
    street = Column(String)
    lat = Column(Float, nullable=True)   # <-- nuova colonna
    lng = Column(Float, nullable=True)   # <-- nuova colonna
    
    owner = relationship("User", back_populates="addresses")