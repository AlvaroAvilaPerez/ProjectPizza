import json
from pathlib import Path
from pydantic import BaseModel
from typing import List, Optional


class Pizza(BaseModel):

    @staticmethod
    def get_pizza_names_from_json(file_path: Path) -> List[str]:
        """Load pizza names from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                pizzas_data = json.load(file)
                return [pizza["name_pizza"] for pizza in pizzas_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading pizza names: {e}")
            return []

    @staticmethod
    def get_pizza_prices_from_json(file_path: Path) -> List[float]:
        """Load pizza prices from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                pizzas_data = json.load(file)
                return [pizza["price"] for pizza in pizzas_data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading pizza prices: {e}")
            return []

    @staticmethod
    def get_pizza_price_by_name(pizza_json_path: Path, pizza_name: str) -> float:
        try:
            with open(pizza_json_path, 'r', encoding="utf-8") as file:
                pizzas_data = json.load(file)
                for pizza in pizzas_data:
                    if pizza.get("name_pizza") == pizza_name:
                        return pizza.get("price", 0.0)
        except FileNotFoundError:
            print(f"Error: {pizza_json_path} not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in pizza data.")
        return 0.0  # Return 0.0 if no matching pizza is found


    @staticmethod
    def get_additional_ingredient_price(json_path: Path, ingredient_name: str) -> float:
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                additional_ingredients = json.load(file)
                for ingredient in additional_ingredients:
                     if ingredient.get("name") == ingredient_name:
                        return ingredient.get("price", 0.0)
                return 0.0  # Default price if ingredient not found
        except FileNotFoundError:
            print(f"Error: {json_path} not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in ingredient data.")
        return 0.0  # Return 0.0 if any error occurs
