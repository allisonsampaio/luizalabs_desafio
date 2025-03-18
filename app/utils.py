from typing import List, Dict
import os

def read_file(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo: {e}")

def validate_file_extension(file_path: str, allowed_extensions: List[str] = ['.txt']) -> bool:
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in allowed_extensions

def parse_line(line: str) -> Dict[str, str]:
    return {
        "user_id": int(line[0:10].strip()),
        "name": line[10:55].strip(),
        "order_id": int(line[55:65].strip()),
        "product_id": int(line[65:75].strip()),
        "value": line[75:87].strip(),
        "date": line[87:95].strip()
    }

def remove_leading_zeros(value: str) -> str:
    return value.lstrip('0')