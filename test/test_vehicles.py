# tests/test_vehicles.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_vehicle():
    response = client.post("/vehicles/", json={
        "id": 1,
        "capacity": 5.0,
        "start_location": [40.4168, -3.7038],
        "max_distance": 100.0
    })
    assert response.status_code == 200
    assert response.json()["vehicle"]["id"] == 1

def test_get_vehicles():
    response = client.get("/vehicles/")
    assert response.status_code == 200
    assert isinstance(response.json()["vehicles"], list)
