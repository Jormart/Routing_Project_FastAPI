# tests/test_routes.py
from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def orders_payload():
    return [
        {"id": 1, "location": [40.4168, -3.7038], "size": 2.5, "time_window": ["09:00", "12:00"]},
        {"id": 2, "location": [39.4699, -0.3757], "size": 1.0, "time_window": ["10:00", "13:00"]}
    ]

@pytest.fixture
def vehicles_payload():
    return [
        {"id": 1, "capacity": 5.0, "start_location": [40.4168, -3.7038], "max_distance": 100.0}
    ]

def test_generate_routes(mocker, orders_payload, vehicles_payload):
    # Mock the distance matrix function to avoid real API call
    mock_distance_matrix = {
        "distances": [[0, 10], [10, 0]]
    }
    mocker.patch("app.services.distance_matrix.get_distance_matrix", return_value=mock_distance_matrix)

    response = client.post("/routes/generate_routes", json={
        "orders": orders_payload,
        "vehicles": vehicles_payload
    })
    assert response.status_code == 200
    assert "routes" in response.json()
