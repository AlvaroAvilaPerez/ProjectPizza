# controllers/order_request.py

from pydantic import BaseModel
from typing import List, Optional


class OrderRequest(BaseModel):
    order_id: int
    order_day: str  # For example "2024-11-20"
    order_number: str
    customer_name: str
    pizzas: list
    extra_ingredients: list
    total: float
