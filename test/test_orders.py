# tests/test_orders.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={
        "id": 1,
        "location": [40.4168, -3.7038],
        "size": 2.5,
        "time_window": ["09:00", "12:00"]
    })
    assert response.status_code == 200
    assert response.json()["order"]["id"] == 1

def test_get_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    assert isinstance(response.json()["orders"], list)

def test_get_order_not_found():
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"
