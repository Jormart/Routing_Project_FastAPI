# POST /vehicles: Create a new vehicle.
# GET /vehicles: Retrieve all vehicles.
# GET /vehicles/{vehicle_id}: Retrieve a single vehicle by ID.

from fastapi import APIRouter, HTTPException
from app.models.vehicle import Vehicle

router = APIRouter()
vehicles = []  # Temporary in-memory storage

@router.post("/")
async def create_vehicle(vehicle: Vehicle):
    vehicles.append(vehicle)
    return {"message": "Vehicle created", "vehicle": vehicle}

@router.get("/")
async def get_vehicles():
    return {"vehicles": vehicles}

@router.get("/{vehicle_id}")
async def get_vehicle(vehicle_id: int):
    vehicle = next((v for v in vehicles if v.id == vehicle_id), None)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


