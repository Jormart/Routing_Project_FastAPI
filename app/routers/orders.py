from fastapi import APIRouter, HTTPException
from app.models.order import Order

router = APIRouter()
orders = []  # Temporary in-memory storage

@router.post("/")
async def create_order(order: Order):
    orders.append(order)
    return {"message": "Order created", "order": order}

@router.get("/")
async def get_orders():
    return {"orders": orders}

@router.get("/{order_id}")
async def get_order(order_id: int):
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
