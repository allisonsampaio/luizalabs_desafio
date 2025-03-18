from pydantic import BaseModel
from typing import List
from .order import Order

class UserOrders(BaseModel):
    user_id: int
    name: str
    orders: List[Order]