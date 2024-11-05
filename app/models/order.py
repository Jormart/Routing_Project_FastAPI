from pydantic import BaseModel
from typing import Optional, Tuple

class Order(BaseModel):
    id: int
    location: Tuple[float, float]  # (latitude, longitude)
    size: float
    time_window: Optional[Tuple[str, str]]  # ("08:00", "10:00")
    area: Optional[str] = None
