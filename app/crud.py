from sqlalchemy.orm import Session
from . import models, schemas

# Retrieve Vehicle details from cache using VIN
def get_vehicle_by_vin(db: Session, vin: str):
  return db.query(models.Vehicle).filter(models.Vehicle.vin == vin).first()

# Create Vehicle in cache
def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
  db_vehicle = models.Vehicle(vin=vehicle.vin, make=vehicle.make, model=vehicle.model, year=vehicle.year, body=vehicle.body, isCached=False)
  db.add(db_vehicle)
  db.commit()
  db.refresh(db_vehicle)
  return db_vehicle

# Update Vehicle isCached field inside cache
def update_vehicle(db: Session, vehicle):
  vehicle.isCached = True
  db.commit()
  db.refresh(vehicle)
  return vehicle

# Remove Vehicle record from cache using VIN
def delete_vehicle_by_vin(db: Session, vehicle):
  db.delete(vehicle)
  db.commit()

# Retrieve all Vehicle records in cache
def get_all_vehicles(db: Session):
  return db.query(models.Vehicle).all()