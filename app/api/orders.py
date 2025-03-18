from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.database.mongo_db import get_order_by_id, get_orders_by_date_range
from app.models.user_orders import UserOrders

router = APIRouter()

@router.get("/{order_id}", response_model=UserOrders)
async def get_order(order_id: int):
    order = get_order_by_id(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Pedido não encontrado")

@router.get("/", response_model=List[UserOrders])
async def get_orders_by_date(
    start_date: str = Query(..., description="Data de início no formato YYYYMMDD"),
    end_date: str = Query(..., description="Data de fim no formato YYYYMMDD")
):
    if not (start_date.isdigit() and len(start_date) == 8 and end_date.isdigit() and len(end_date) == 8):
        raise HTTPException(status_code=422, detail="Formato de data inválido. Use YYYYMMDD.")

    orders = get_orders_by_date_range(start_date, end_date)
    if orders:
        return orders
    raise HTTPException(status_code=404, detail="Nenhum pedido encontrado no intervalo de datas especificado")