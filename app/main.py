
from fastapi import FastAPI
from app.routers import orders, vehicles, routes  # Import the new router

# Load environment variables from the .env file
load_dotenv()

app = FastAPI(title="Routing Optimization API")

app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(routes.router, prefix="/routes", tags=["Routes"])  # Include routes router
