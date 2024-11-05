# Routing Optimization Project

This project is a routing optimization backend service inspired by Mercadona Tech's routing system for efficient delivery scheduling. The service calculates optimized delivery routes for a list of orders, considering constraints like delivery windows, vehicle capacities, and geographic clustering.\
Further information in this article: [routing-lechugas-at-mercadona-tech](https://medium.com/mercadona-tech/routing-lechugas-at-mercadona-tech-b676174e470b)

## Features

- **Order Management**: Create and retrieve delivery orders.
- **Vehicle Management**: Define and retrieve available delivery vehicles.
- **Routing Optimization**: Calculate optimal delivery routes based on a time-distance matrix and vehicle constraints.
- **Distance Matrix Integration**: Uses OpenRouteService (ORS) to fetch travel times and distances between delivery locations.

---

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [API Documentation](#api-documentation)
    - [Order Endpoints](#order-endpoints)
    - [Vehicle Endpoints](#vehicle-endpoints)
    - [Route Calculation Endpoint](#route-calculation-endpoint)
5. [Testing](#testing)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd mercadona_routing_project
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   - This project requires an ORS (OpenRouteService) API key. Set the `ORS_API_KEY` environment variable in your shell or a `.env` file.
     ```bash
     export ORS_API_KEY="your_ors_api_key"
     ```

5. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

---

## Project Structure

```plaintext
mercadona_routing_project/
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── routers/
│   │   ├── orders.py          # Order management endpoints
│   │   ├── vehicles.py        # Vehicle management endpoints
│   │   └── routes.py          # Route optimization endpoint
│   ├── services/
│   │   ├── distance_matrix.py # ORS integration for distance matrix
│   │   └── routing_engine.py  # Routing optimization logic
│   ├── models/
│   │   ├── order.py           # Order data model
│   │   └── vehicle.py         # Vehicle data model
│   └── utils/
│       └── clustering.py      # Optional clustering logic
├── tests/
│   ├── test_orders.py         # Tests for order endpoints
│   ├── test_vehicles.py       # Tests for vehicle endpoints
│   ├── test_routes.py         # Tests for route calculation
│   ├── test_distance_matrix.py# Tests for distance matrix service
│   ├── test_routing_engine.py # Tests for routing engine
│   └── conftest.py            # Pytest fixtures
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Usage

The project provides a REST API for managing orders, vehicles, and generating optimized routes.

1. **Add Orders**: Create new delivery orders with location, size, and time window information.
2. **Add Vehicles**: Define available vehicles with capacity, starting location, and distance constraints.
3. **Generate Routes**: Calculate optimized delivery routes based on the defined orders and vehicles.

---

## API Documentation

### Order Endpoints

- **Create Order**  
  `POST /orders/`  
  Creates a new delivery order.
  
  **Request Body**:
  ```json
  {
    "id": 1,
    "location": [40.4168, -3.7038],
    "size": 2.5,
    "time_window": ["09:00", "12:00"]
  }
  ```

  **Response**:
  ```json
  {
    "message": "Order created",
    "order": {
      "id": 1,
      "location": [40.4168, -3.7038],
      "size": 2.5,
      "time_window": ["09:00", "12:00"]
    }
  }
  ```

- **Retrieve All Orders**  
  `GET /orders/`  
  Retrieves a list of all orders.

- **Retrieve Single Order**  
  `GET /orders/{order_id}`  
  Retrieves details for a specific order.

### Vehicle Endpoints

- **Create Vehicle**  
  `POST /vehicles/`  
  Creates a new delivery vehicle.
  
  **Request Body**:
  ```json
  {
    "id": 1,
    "capacity": 5.0,
    "start_location": [40.4168, -3.7038],
    "max_distance": 100.0
  }
  ```

  **Response**:
  ```json
  {
    "message": "Vehicle created",
    "vehicle": {
      "id": 1,
      "capacity": 5.0,
      "start_location": [40.4168, -3.7038],
      "max_distance": 100.0
    }
  }
  ```

- **Retrieve All Vehicles**  
  `GET /vehicles/`  
  Retrieves a list of all vehicles.

### Route Calculation Endpoint

- **Generate Optimized Routes**  
  `POST /routes/generate_routes`  
  Calculates optimized routes based on provided orders and vehicles.
  
  **Request Body**:
  ```json
  {
    "orders": [
      {"id": 1, "location": [40.4168, -3.7038], "size": 2.5, "time_window": ["09:00", "12:00"]},
      {"id": 2, "location": [39.4699, -0.3757], "size": 1.0, "time_window": ["10:00", "13:00"]}
    ],
    "vehicles": [
      {"id": 1, "capacity": 5.0, "start_location": [40.4168, -3.7038], "max_distance": 100.0}
    ]
  }
  ```

  **Response**:
  ```json
  {
    "routes": [
      [
        {"order_id": 1, "location": [40.4168, -3.7038], "time_window": ["09:00", "12:00"], "size": 2.5},
        {"order_id": 2, "location": [39.4699, -0.3757], "time_window": ["10:00", "13:00"], "size": 1.0}
      ]
    ]
  }
  ```

---

## Testing

To ensure all components work as expected, the project includes a comprehensive test suite.

1. **Run Tests**:
   ```bash
   pytest
   ```

2. **Test Structure**:
   - `tests/test_orders.py`: Tests for order management endpoints.
   - `tests/test_vehicles.py`: Tests for vehicle management endpoints.
   - `tests/test_routes.py`: Tests for route calculation.
   - `tests/test_distance_matrix.py`: Tests for the distance matrix service, including mocks for API calls.
   - `tests/test_routing_engine.py`: Tests the core routing algorithm logic.

3. **Fixtures**:
   - `tests/conftest.py` contains reusable fixtures, like sample orders and vehicles, for testing.

---

## Future Improvements

This project can be expanded with:

- **Manual Adjustment Interface**: A frontend for visualizing and manually adjusting routes before final optimization.
- **Caching**: Store frequently used distance matrices to minimize external API calls.
- **Enhanced Error Handling**: More robust handling of invalid inputs and external API failures.

---

## License

This project is licensed under the MIT License.

---

## Contact

For any questions or contributions, please reach me out.
