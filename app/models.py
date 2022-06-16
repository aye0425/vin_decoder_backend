from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class Vehicle(Base):
  __tablename__ = 'vehicles'

  id = Column(Integer, primary_key=True, index=True)
  vin = Column(String(17), unique=True, index=True)
  make = Column(String)
  model = Column(String)
  year = Column(String)
  body = Column(String)
  isCached = Column(Boolean)