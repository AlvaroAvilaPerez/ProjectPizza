# builders/pizza_builder.py

from models.pizza import Pizza


class PizzaBuilder:
    def __init__(self, name, base_price, ingredients):
        self.pizza = Pizza(name=name, base_price=base_price, ingredients=ingredients)

    def add_extra_ingredient(self, ingredient):
        """
          Adds extra ingredient to the pizza.
          Allows chaining of methods.
        """
        self.pizza.add_extra_ingredient(ingredient)
        return self

    def build(self):
        """
         Returns the pizza object after modifications.
         """
        self.pizza.calculate_price()  # Recalculate price after modifications
        return self.pizza  # Return the pizza object with the updated price


