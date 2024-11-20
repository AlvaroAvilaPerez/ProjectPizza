
from collections import Counter
from pathlib import Path

from models.pizza import Pizza
from models.pizza_order import PizzaOrder


class Promotion:

    promotions = {
        "Promotion 2x1": "Buy two pizzas and get another one "
                         "free (applies to pizzas of the same type on Tuesdays and Wednesdays).",
        "Free Delivery": "Free delivery every Thursday."
    }

    def apply_two_for_one_promotion(self, pizza_json_path: Path, order: PizzaOrder) -> float:
        total_price = 0.0
        if order.is_tuesday_or_wednesday():
            modified_counts = self.modify_counts(order.pizzas)
            for pizza, count in modified_counts.items():
                pizza_price = Pizza.get_pizza_price_by_name(pizza_json_path, pizza)
                if pizza_price > 0:
                    promo_count = count // 2 + count % 2  # Apply 2-for-1 promotion
                    total_price += promo_count * pizza_price
        else:
            for pizza in order.pizzas:
                pizza_price = Pizza.get_pizza_price_by_name(pizza_json_path, pizza)
                if pizza_price > 0:
                    total_price += pizza_price

        return total_price

    def count_pizzas(self, pizza_list):
        pizza_counts = Counter(pizza_list)
        return pizza_counts

    def modify_counts(self, pizza_list):

        pizza_counts = self.count_pizzas(pizza_list)
        modified_counts = {}

        for pizza, count in pizza_counts.items():
            if count % 2 == 0:
                modified_counts[pizza] = count // 2
            elif count > 3:
                modified_counts[pizza] = ((count - 1) // 2) + 1
            else:
                modified_counts[pizza] = count
        return modified_counts

    def apply_delivery_cost_promotion(self, order: PizzaOrder) -> float:
        if order.is_thursday():
            return 0.0  # Free delivery on Thursday
        else:
            return order.get_delivery_cost()


