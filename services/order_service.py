import json
from pathlib import Path
from typing import List, Optional, Dict
from models.pizza_order import PizzaOrder
from models.promotion import Promotion


class OrderService:
    def __init__(self, pizza_json_path: Path, ingredients_json_path: Path):
        """

        :rtype: object
        """
        self.pizza_json_path = pizza_json_path
        self.ingredients_json_path = ingredients_json_path
        self.orders = []  # Initialize the orders list

    def load_ingredients(self) -> List[dict]:
        """
        Load the list of ingredients from the ingredients JSON file.
        :return: List of ingredient dictionaries.
        """
        try:
            with open(self.ingredients_json_path, 'r', encoding='utf-8') as file:
                ingredients = json.load(file)
                return ingredients
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading ingredients: {e}")
            return []

    def calculate_total_price(self, order: PizzaOrder, promotion: Promotion) -> float:

        pizza_total = promotion.apply_two_for_one_promotion(self.pizza_json_path, order)
        delivery_cost = promotion.apply_delivery_cost_promotion(order)
        ingredient_cost = PizzaOrder.calculate_total_ingredients(self.ingredients_json_path, order)

        total_price = pizza_total + delivery_cost + ingredient_cost
        return total_price

    def create_order(self, order_data: Dict) -> PizzaOrder:
        order = PizzaOrder(
            order_number=order_data["order_number"],
            order_date=order_data["order_date"],
            customer_name=order_data["customer_name"],
            pizzas=order_data["pizzas"],
            additional_ingredients=order_data.get("additional_ingredients", []),
            address=order_data["address"]
        )
        promotion = Promotion()
        total_price = self.calculate_total_price(order, promotion)
        order.total = total_price
        return order

    def save_order(self, file_path: str, order: PizzaOrder):
        try:
            with open(file_path, 'r') as file:
                orders = json.load(file)
        except FileNotFoundError:
            orders = []

        orders.append(order.dict())
        with open(file_path, 'w') as file:
            json.dump(orders, file, indent=4)

        print(f"Order {order.order_number} has been added successfully!")

    def create_order_and_save(self, file_path: str, order_data: Dict):

        order = self.create_order(order_data)  # Crear la orden
        self.save_order(file_path, order)  # Guardar la orden en el archivo

