from typing import Dict

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