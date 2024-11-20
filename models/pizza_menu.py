from pathlib import Path
from models.pizza import Pizza
from models.promotion import Promotion


class PizzaMenu:
    """
    Class that manages the pizza menu with prices, ingredients, and available promotions.
    """

    def __init__(self, pizza_data_path: Path, ingredient_data_path: Path):
        self.pizza_data_path = pizza_data_path
        self.ingredient_data_path = ingredient_data_path
        self.pizza = Pizza()  # Instance of the Pizza class
        self.promotion = Promotion()  # Instance of the Promotion class

    def show_menu(self):
        """Displays the pizza menu, including ingredients and promotions."""
        print("\n--- Pizza Menu ---")
        # Check if files exist
        if not self.pizza_data_path.exists() or not self.ingredient_data_path.exists():
            print(f"Error: One or both files not found.\nPizza Data File: {self.pizza_data_path}\nIngredient Data File: {self.ingredient_data_path}")
            return  # Exit early if files are missing

        # Display pizza types and their prices
        self.show_pizza_types()

        # Display ingredients and their prices
        self.show_ingredients()

        # Display available promotions
        self.show_promotions()

    def show_pizza_types(self):
        """Display the pizza types and their prices from the JSON file."""
        pizza_names = Pizza.get_pizza_names_from_json(self.pizza_data_path)
        pizza_prices = Pizza.get_pizza_prices_from_json(self.pizza_data_path)

        if pizza_names and pizza_prices:
            print("\nPizza Types and Prices:")
            for name, price in zip(pizza_names, pizza_prices):
                print(f"{name}: ${price}")
        else:
            print("Could not retrieve pizza information.")

    def show_ingredients(self):
        """Display the ingredient names and their prices from the JSON file."""
        ingredient_names = Pizza.get_ingredient_names_from_json(self.ingredient_data_path)
        ingredient_prices = Pizza.get_ingredient_prices_from_json(self.ingredient_data_path)

        if ingredient_names and ingredient_prices:
            print("\nIngredients and Prices:")
            for name, price in zip(ingredient_names, ingredient_prices):
                print(f"{name}: ${price}")
        else:
            print("Could not retrieve ingredient information.")

    def show_promotions(self):
        """Display the available promotions."""
        promotions = Promotion.promotions  # Assuming Promotion class has this method
        if promotions:
            print("\nPromotions:")
            for promo in promotions:
                print(promo)
        else:
            print("No promotions available.")
