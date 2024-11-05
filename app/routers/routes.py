from fastapi import APIRouter, HTTPException, Depends
from app.services.distance_matrix import get_distance_matrix
from app.services.routing_engine import calculate_routes
from app.models.order import Order
from app.models.vehicle import Vehicle
from typing import List

router = APIRouter()

@router.post("/generate_routes")
async def generate_routes(
    orders: List[Order],
    vehicles: List[Vehicle]
):
    # Check if orders and vehicles are provided
    if not orders:
        raise HTTPException(status_code=400, detail="No orders provided.")
    if not vehicles:
        raise HTTPException(status_code=400, detail="No vehicles provided.")

    # Extract locations from orders
    locations = [order.location for order in orders]

    # Retrieve distance matrix
    try:
        distance_matrix_data = get_distance_matrix(locations)
        distance_matrix = distance_matrix_data['distances']
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch distance matrix.")

    # Define number of vehicles and depot
    num_vehicles = len(vehicles)
    depot_index = 0

    # Calculate routes using the routing engine
    try:
        routes = calculate_routes(distance_matrix, num_vehicles, depot=depot_index)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Routing optimization failed.")

    # Format routes for better readability
    formatted_routes = format_routes(routes, orders)
    return {"routes": formatted_routes}

def format_routes(routes, orders):
    formatted_routes = []
    for vehicle_route in routes:
        route_info = []
        for order_index in vehicle_route:
            order = orders[order_index]
            route_info.append({
                "order_id": order.id,
                "location": order.location,
                "time_window": order.time_window,
                "size": order.size
            })
        formatted_routes.append(route_info)
    return formatted_routes
