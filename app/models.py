from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    product_id: int
    value: str

class Order(BaseModel):
    order_id: int
    total: str
    date: str
    products: List[Product]

class UserOrders(BaseModel):
    user_id: int
    name: str
    orders: List[Order]