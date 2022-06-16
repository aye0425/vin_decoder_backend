from pydantic import BaseModel, validator

class VehicleBase(BaseModel):
  vin: str

  @validator('vin')
  def validate_vin(cls, v):
    if len(v) is not 17:
      raise ValueError('Must be 17 characters')

    if not v.isalnum():
      raise ValueError('Must be alphanumeric')

    return v.title()

class VehicleCreate(VehicleBase):
  make: str
  model: str
  year: str
  body: str
  isCached: bool

class Vehicle(VehicleBase):
  id: int
  make: str
  model: str
  year: str
  body: str
  isCached: bool

  class Config:
    orm_mode = True
