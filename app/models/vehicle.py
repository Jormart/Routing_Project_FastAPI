from pydantic import BaseModel
from typing import Tuple, Optional

class Vehicle(BaseModel):
    id: int
    capacity: float
    start_location: Tuple[float, float]  # (latitude, longitude)
    max_distance: Optional[float] = None
