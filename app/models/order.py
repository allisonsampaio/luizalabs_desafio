from pydantic import BaseModel
from typing import List
from .product import Product

class Order(BaseModel):
    order_id: int
    total: str
    date: str
    products: List[Product]