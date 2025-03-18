import pytest
from app.services import process_file
from app.models import UserOrders, Order, Product

def test_process_file():
    """
    Testa a função process_file para garantir que o arquivo é processado corretamente
    """
    file_path = "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("0000000070                              Palmer Prosacco00000007530000000003     1836.7420210308\n")
        file.write("0000000075                                  Bobbie Batz00000007980000000002     1578.5720211116\n")

    result = process_file(file_path)

    assert len(result) == 2

    assert result[0].user_id == 70
    assert result[0].name == "Palmer Prosacco"
    assert len(result[0].orders) == 1
    assert result[0].orders[0].order_id == 753
    assert result[0].orders[0].total == "1836.74"
    assert len(result[0].orders[0].products) == 1
    assert result[0].orders[0].products[0].product_id == 3
    assert result[0].orders[0].products[0].value == "1836.74"

    assert result[1].user_id == 75
    assert result[1].name == "Bobbie Batz"
    assert len(result[1].orders) == 1
    assert result[1].orders[0].order_id == 798
    assert result[1].orders[0].total == "1578.57"
    assert len(result[1].orders[0].products) == 1
    assert result[1].orders[0].products[0].product_id == 2
    assert result[1].orders[0].products[0].value == "1578.57"

    import os
    os.remove(file_path)

def test_process_file_empty():
    """
    Testa a função process_file com um arquivo vazio
    """
    file_path = "empty_file.txt"
    with open(file_path, 'w') as file:
        file.write("")

    result = process_file(file_path)

    assert result == []

    import os
    os.remove(file_path)

def test_process_file_invalid_format():
    """
    Testa a função process_file com um arquivo de formato inválido
    """
    file_path = "invalid_file.txt"
    with open(file_path, 'w') as file:
        file.write("invalid,data\n1,2,3")

    result = process_file(file_path)

    assert result == []

    import os
    os.remove(file_path)