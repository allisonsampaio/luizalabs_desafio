from pymongo import MongoClient
from app.models.user_orders import UserOrders
from typing import List
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["order_db"]
orders_collection = db["orders"]

def save_orders_to_db(orders: List[UserOrders]):
    for user_order in orders:
        order_data = user_order.model_dump()
        orders_collection.insert_one(order_data)

def get_order_by_id(order_id: int):
    return orders_collection.find_one({"orders.order_id": order_id})

def get_orders_by_date_range(start_date: str, end_date: str):
    return list(orders_collection.find({
        "orders": {
            "$elemMatch": {
                "date": {
                    "$gte": start_date,
                    "$lte": end_date
                }
            }
        }
    }))