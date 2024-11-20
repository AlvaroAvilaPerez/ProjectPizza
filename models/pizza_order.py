import os
from datetime import datetime
from typing import Union, List
from typing import Optional, ClassVar, Dict
from pydantic import BaseModel
from pathlib import Path
import json

from models.pizza import Pizza


class PizzaOrder(BaseModel):
    id: Optional[int] = None
    order_number: Optional[str] = None
    order_date: Optional[str] = None
    customer_name: Optional[str] = None
    pizzas: List[str] = []
    additional_ingredients: Optional[List[str]] = []
    address: Optional[str] = None
    total: Optional[float] = 0.0

    json_file_path: ClassVar[Path] = Path("models/orderdb.json")
    date_format: ClassVar[str] = "%Y-%m-%d"  # Define the date format here

    class Config:
        from_attributes = True

    def set_order_date(self, order_date: Optional[str]) -> datetime:
        """Converts the provided date to a datetime object or uses today's date if not provided."""
        if order_date:
            if isinstance(order_date, str):
                return datetime.strptime(order_date, self.date_format)
        return datetime.today()  # Default to today's date if no date is provided

    def is_tuesday_or_wednesday(self) -> bool:
        """Returns True if the order date is Tuesday or Wednesday."""
        order_date = self.set_order_date(self.order_date)
        return order_date.weekday() in [1, 2]  # Tuesday (1) and Wednesday (2)

    def is_thursday(self) -> bool:
        """Returns True if the order date is Thursday."""
        order_date = self.set_order_date(self.order_date)
        return order_date.weekday() == 3  # Thursday

    def count_pizzas(self) -> int:
        """Counts the total number of pizzas in the order."""
        return len(self.pizzas)

    def get_delivery_cost(self) -> float:
        return 15.0 if self.address else 0.0

    def order_date_summary(self) -> str:
        """Returns a summary of the order date and delivery cost."""
        order_date = self.set_order_date(self.order_date)
        return f"Order Date: {order_date.strftime(self.date_format)}\nDelivery Cost: ${self.get_delivery_cost():.2f}"

    def add_ingredient_to_pizza(self, pizza_name: str, ingredient_name: str):
        # Add ingredient to pizza (you can implement your own logic here)
        self.ingredients.append(ingredient_name)

    def calculate_total_ingredients(json_path: Path, ingredient_names: list) -> float:
        total_cost = 0.0
        for ingredient_name in ingredient_names:
            price = Pizza.get_additional_ingredient_price(json_path, ingredient_name)
            total_cost += price
        return total_cost


def check_and_create_order_db(file_path: str):

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)
        print(f"File {file_path} created successfully.")
    else:
        print(f"File {file_path} already exists.")


