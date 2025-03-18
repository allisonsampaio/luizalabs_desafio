import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_file_success():
    """
    Testa o endpoint /upload com um arquivo válido
    """
    test_file_content = (
        "0000000070                              Palmer Prosacco00000007530000000003     1836.7420210308\n"
        "0000000075                                  Bobbie Batz00000007980000000002     1578.5720211116\n"
    )

    response = client.post(
        "/upload",
        files={"file": ("test_file.txt", test_file_content)}
    )

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2

    assert data[0]["user_id"] == 70
    assert data[0]["name"] == "Palmer Prosacco"
    assert len(data[0]["orders"]) == 1
    assert data[0]["orders"][0]["order_id"] == 753
    assert data[0]["orders"][0]["total"] == "1836.74"
    assert len(data[0]["orders"][0]["products"]) == 1
    assert data[0]["orders"][0]["products"][0]["product_id"] == 3
    assert data[0]["orders"][0]["products"][0]["value"] == "1836.74"

    assert data[1]["user_id"] == 75
    assert data[1]["name"] == "Bobbie Batz"
    assert len(data[1]["orders"]) == 1
    assert data[1]["orders"][0]["order_id"] == 798
    assert data[1]["orders"][0]["total"] == "1578.57"
    assert len(data[1]["orders"][0]["products"]) == 1
    assert data[1]["orders"][0]["products"][0]["product_id"] == 2
    assert data[1]["orders"][0]["products"][0]["value"] == "1578.57"

def test_get_order_by_id():
    """
    Testa o endpoint /orders/{order_id} para buscar um pedido pelo ID
    """
    response = client.get("/orders/753")
    assert response.status_code == 200
    data = response.json()
    assert data["orders"][0]["order_id"] == 753

def test_get_orders_by_date_range():
    """
    Testa o endpoint /orders/ para buscar pedidos por intervalo de datas
    """
    response = client.get("/orders/?start_date=20210101&end_date=20211231")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0