from typing import List
from app.models.user_orders import UserOrders
from app.models.order import Order
from app.models.product import Product
from app.utils.file_utils import parse_line
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_file(file_path: str) -> List[UserOrders]:
    users = {}
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if len(line.strip()) == 0:
                logger.warning(f"Ignorando linha {line_number}: linha vazia.")
                continue

            try:
                parsed_data = parse_line(line)
                logger.info(f"Linha {line_number} parseada com sucesso: {parsed_data}")

                user_id = parsed_data["user_id"]
                name = parsed_data["name"]
                order_id = parsed_data["order_id"]
                product_id = parsed_data["product_id"]
                value = parsed_data["value"]
                date = parsed_data["date"]

                if user_id not in users:
                    users[user_id] = UserOrders(user_id=user_id, name=name, orders=[])

                order = next((o for o in users[user_id].orders if o.order_id == order_id), None)
                if not order:
                    order = Order(order_id=order_id, total=value, date=date, products=[])
                    users[user_id].orders.append(order)

                product = Product(product_id=product_id, value=value)
                order.products.append(product)
            except (ValueError, IndexError) as e:
                logger.error(f"Erro ao processar linha {line_number}: {e}. Linha: {line.strip()}")
                continue

    return list(users.values())