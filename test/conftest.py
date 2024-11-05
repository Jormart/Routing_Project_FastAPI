# tests/conftest.py
import pytest
from app.models.order import Order
from app.models.vehicle import Vehicle

@pytest.fixture
def sample_orders():
    return [
        Order(id=1, location=(40.4168, -3.7038), size=2.5, time_window=("09:00", "12:00")),
        Order(id=2, location=(39.4699, -0.3757), size=1.0, time_window=("10:00", "13:00"))
    ]

@pytest.fixture
def sample_vehicles():
    return [
        Vehicle(id=1, capacity=5.0, start_location=(40.4168, -3.7038), max_distance=100.0)
    ]
