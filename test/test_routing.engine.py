# tests/test_routing_engine.py
from app.services.routing_engine import calculate_routes

def test_calculate_routes(sample_orders, sample_vehicles):
    # Mock distance matrix as a symmetric matrix
    distance_matrix = [
        [0, 10],
        [10, 0]
    ]
    num_vehicles = len(sample_vehicles)
    depot_index = 0

    routes = calculate_routes(distance_matrix, num_vehicles, depot=depot_index)
    assert routes is not None
    assert isinstance(routes, list)
