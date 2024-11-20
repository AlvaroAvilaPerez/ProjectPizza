# # ProjectPizza/test_example.py
#
# from pathlib import Path
# from models.pizza import Pizza
# from models.pizza_menu import PizzaMenu
# from models.pizza_order import PizzaOrder
# from models.promotion import Promotion
# from services.order_service import OrderService
#
#
# BASE_DIR = Path(__file__).resolve().parent
# json_file_path = BASE_DIR / "models/type_pizza.json"
#
#
#
# print("********************************************")
# # Ejemplo 1: Pasar una fecha en formato de cadena
# order = PizzaOrder()
# date_str = "2024-11-19"  # Fecha en formato string
# order_date = order.set_order_date(date_str)
# print(f"Fecha del pedido: {order_date}")  # Debería imprimir "2024-11-19 00:00:00"
#
#
# print("********************************************")
# # Test case 1: No address, no date provided (default date is today, Friday)
# order1 = PizzaOrder()  # No address provided
# print(order1.order_date_summary())  # Expected: $0.0 (no address)
#
# # Test case 2: With address, no date provided (default date is today, Friday)
# order2 = PizzaOrder(address="123 Main St")  # Address provided
# print(order2.order_date_summary())  # Expected: $15.0 (Friday)
#
# # Test case 3: No address, with specific date (Thursday)
# order3 = PizzaOrder(order_date="2024-11-14")  # No address, delivery on Thursday
# print(order3.order_date_summary())  # Expected: $0.0 (no address)
#
# # Test case 4: With address, with specific date (Thursday)
# order4 = PizzaOrder(order_date="2024-11-14", address="123 Main St")  # With address, Thursday
# print(order4.order_date_summary())  # Expected: $0.0 (with address)
#
# print("********************************************")
#
#
# pizza_names = Pizza.get_pizza_names_from_json(json_file_path)
# pizza_prices = Pizza.get_pizza_prices_from_json(json_file_path)
# print("Pizza Names:", pizza_names)
# print("Pizza prices:", pizza_prices)
#
# BASE_DIR = Path(__file__).resolve().parent
# json_file_path1 = BASE_DIR / "models/ingredients_pizza.json"
#
# ingredient_names = Pizza.get_ingredient_names_from_json(json_file_path1)
# ingredient_prices = Pizza.get_ingredient_prices_from_json(json_file_path1)
#
# print(ingredient_names)  # Output: ['Tomato', 'Olives', 'Cheese']
# print(ingredient_prices)  # Output: [2, 2, 3]
# # -----------------------------------------------------
# print("********************************************")
# # Create an instance of Pizza
# pizza = Pizza()
#
# # Get the price of an existing pizza
# margarita_price = pizza.get_pizza_price_by_name(json_file_path, "Margherita")
# print(f"Margarita Price: ${margarita_price}")
#
# # Attempt to get the price of a non-existent pizza
# veggie_price = pizza.get_pizza_price_by_name(json_file_path, "Veggie")
# print(f"Veggie Price: ${veggie_price}")
#
# # =============================================================
# print("******************testttt**************************")
# # Example usage
# order1 = PizzaOrder(order_date="2024-11-15", pizzas=["Margherita", "Margherita"])
# pizza_count1 = order1.count_pizzas()
# print(f"Pizza Count: {pizza_count1} | Total Pizzas: {pizza_count1}")
#
# order2 = PizzaOrder(order_date="2024-11-14", pizzas=["Pepperoni", "Margherita"])
# pizza_count2 = order2.count_pizzas()
# print(f"Pizza Count: {pizza_count2} | Total Pizzas: {pizza_count2}")
#
# order3 = PizzaOrder(order_date="2024-11-13", pizzas=["Margherita", "Pepperoni", "Simple"])
# pizza_count3 = order3.count_pizzas()
# print(f"Pizza Count: {pizza_count3} | Total Pizzas: {pizza_count3}")
# # ___________________________________________________________________
#
# print("*****************PizzaOrder***************************")
# # Create the PizzaOrder instance and pass it to the OrderService
#
# promotion = Promotion()  # You need to create a Promotion instance, assuming it has been defined elsewhere
#
#
# # # Test case 1: Thursday (2024-11-14)
# # order1 = PizzaOrder(order_date="2024-11-14", pizzas=["Margherita", "Margherita"], address="123 Main St")
# # order_service1 = OrderService(promotion=promotion, pizza_json_path=json_file_path)
# # total_price1 = order_service1.calculate_total_price(order1)
# # print(f"Total Price (Thursday, 2 Margheritas + Free Delivery): ${total_price1}")  # Expected: $16.0
# #
# # # Test case 2: Friday (2024-11-15)
# # order2 = PizzaOrder(order_date="2024-11-15", pizzas=["Margherita", "Pepperoni"], address="123 Main St")
# # order_service2 = OrderService(order2, json_file_path)
# # total_price2 = order_service2.calculate_total_price(order1)
# # print(f"Total Price (Friday, Margheritas + Pepperoni + Delivery Fee): ${total_price2}")  # Expected: $32.0
# #
# # # Test case 3: Wednesday (2024-11-13)
# # order3 = PizzaOrder(order_date="2024-11-13", pizzas=["Margherita", "Pepperoni", "Pepperoni"], address="123 Main St")
# # order_service3 = OrderService(order3, json_file_path)
# # total_price3 = order_service3.calculate_total_price(order1)
# # print(f"Total Price (Wednesday, Margheritas + 2x1 Pepperoni + Delivery Fee): ${total_price3}")  # Expected: $32.0
#
#
# print("*****************show_menu***************************")
#
# # Correct paths to the files based on your current working directory
# BASE_DIR = Path(__file__).resolve().parent
# json_file_path1 = BASE_DIR / "models/ingredients_pizza.json"
#
# # Instantiate and show the pizza menu
# menu = PizzaMenu(json_file_path, json_file_path1)
# menu.show_menu()
#
# print("******************count_pizzas**************************")
#
# # Example usage
# pizza_list_3 = ["Margherita", "Margherita", "Margherita", "Margherita", "Pepperoni"]
#
# promotion = Promotion()
#
# # Count pizzas in the list
# pizza_count = promotion.count_pizzas(pizza_list_3)
#
# print(pizza_count)  # Output: Counter({'Margherita': 4, 'Pepperoni': 1})
#
# print("**************apply_two_for_one_promotion******************************")
#
# # Example pizza order
# pizza_list_34 = ["Margherita", "Margherita", "Pepperoni", "Pepperoni", "Simple"]
# order_date_str = "2024-11-19"  # Example order date (can be set dynamically)
#
# # Initialize the PizzaOrder using keyword arguments
# order = PizzaOrder(pizzas=pizza_list_34, order_date=order_date_str)
#
# promotion = Promotion()
#
# total_price = promotion.apply_two_for_one_promotion(json_file_path, order)
#
# print(f"Total price: {total_price}")
#
#
# pizza_list_32 = ["Margherita", "Margherita"]
# order_date_str2 = "2024-11-14"  # Order date for Thursday
# order2 = PizzaOrder(pizzas=pizza_list_32, order_date=order_date_str2)
#
# total_price2 = promotion.apply_two_for_one_promotion(json_file_path, order2)
#
# print(f"Total price: {total_price2}")
#
# print("**************apply_delivery_cost_promotion******************************")
#
#
#
#
# # Crear una orden de ejemplo
# pizza_order = PizzaOrder(
#     order_date="2024-11-19",  # Jueves
#     address="123 Pizza Street",
#     pizzas=["Margherita", "Margherita", "Pepperoni", "Pepperoni", "Pepperoni"]
# )
#
# # Instanciar la clase Promotion
# promotion = Promotion()
#
#
# # Aplicar la promoción de envío gratuito
# delivery_cost = promotion.apply_delivery_cost_promotion(pizza_order)
# print(f"Delivery Cost: ${delivery_cost:.2f}")
#
# print("**************tutuss******************************")
# #
# # order = PizzaOrder(order_date="2024-11-14", pizzas=["Margherita", "Pepperoni", "Pepperoni"], address="123 Main St")
# #
# #
# # order_service = OrderService(order, json_file_path)
# # total_price = order_service.calculate_total_price()
# #
# # print(f"Total price: ${total_price:.2f}")
# #
# #
# # order = PizzaOrder(order_date="2024-11-19", pizzas=["Margherita", "Margherita", "Pepperoni", "Pepperoni"], address="123 Main St")
# #
# #
# # order_service = OrderService(order, json_file_path)
# # total_price = order_service.calculate_total_price()
# #
# # print(f"Total price: ${total_price:.2f}")
#
# print("**************tutussa******************************")
#
#
# print("*****************PizzaOrder***************************")
# # Create the PizzaOrder instance and pass it to the OrderService
#
# promotion = Promotion()  # You need to create a Promotion instance, assuming it has been defined elsewhere
#
#
#
# # Create the PizzaOrder instance
# order1 = PizzaOrder(order_date="2024-11-14", pizzas=["Margherita", "Margherita", "Pepperoni"], address="123 Main St")
#
# # Create the OrderService instance, passing the pizza_json_path
# order_service12 = OrderService(pizza_json_path=json_file_path)
#
# # Calculate the total price with the promotion instance
# total_price1 = order_service12.calculate_total_price(order1, promotion)
#
# # Output the total price
# print(f"Total Price ${total_price1}")  # Expected: $16.0
#
# print("*****************AddOrder***************************")
#
#
# # Example usage
# pizza_json_path = Path("pedidos.json")
# order_service = OrderService(pizza_json_path)
#
# # Create a new order
# order = order_service.add_order(
#     customer_name="Juan Pérez",
#     pizzas=["Margherita", "Margherita", "Pepperoni"],
#     order_date="2024-11-14",
#     address="123 Main St"
# )
#
# # Print order details
# print(f"Order ID: {order.id}")
# print(f"Order Number: {order.order_number}")
# print(f"Customer Name: {order.customer_name}")
# print(f"Pizzas: {order.pizzas}")
# print(f"Total Price: ${order.total:.2f}")
from pathlib import Path
from models.pizza import Pizza
from models.pizza_order import PizzaOrder
from models.promotion import Promotion
from services.order_service import OrderService
from services.order_service import OrderService

json_path = Path("models/type_pizza.json")
additional_ingredients_path = Path("models/ingredients_pizza.json")

print("-----------get_pizza_names_from_json---get_pizza_price_by_name--get_ingredients_by_pizza_name------")

# Get all pizza names
pizza_names = Pizza.get_pizza_names_from_json(json_path)
print("Pizza Names:", pizza_names)

# Get the price of a specific pizza
price = Pizza.get_pizza_price_by_name(json_path, "Margherita")
print("Price of Margherita:", price)

# # Get the ingredients of a specific pizza
# ingredients = Pizza.get_ingredients_by_pizza_name(json_path, "Margherita")
# print("Ingredients of Margherita:", ingredients)

print("-----get_additional_ingredient_price-------")

ingredient_name = "basil"
price = Pizza.get_additional_ingredient_price(additional_ingredients_path, ingredient_name)
print(f"The price of '{ingredient_name}' is ${price:.2f}")

print("-----calculate_total_ingredients-------")

ingredients_to_add = ["pineapple", "peppers", "basil"]
total_ingredients_cost = PizzaOrder.calculate_total_ingredients(additional_ingredients_path, ingredients_to_add)
print(f"Total cost for ingredients {ingredients_to_add}: ${total_ingredients_cost:.2f}")

ingredients_to_add = ["pineapple"]
total_ingredients_cost = PizzaOrder.calculate_total_ingredients(additional_ingredients_path, ingredients_to_add)
print(f"Total cost for ingredients {ingredients_to_add}: ${total_ingredients_cost:.2f}")

print("-----------------------is_tuesday_or_wednesday--------------------------------------")

order1 = PizzaOrder(
        pizzas=["Pepperoni", "Margarita"],
        order_date="2024-11-14",  # Jueves
        address="Street 1"
    )
order2 = PizzaOrder(
    pizzas=["Hawaiian", "Veggie"],
    order_date="2024-11-13",  # Miércoles
    address="Street 2"
)
order3 = PizzaOrder(
     pizzas=["BBQ Chicken"],
     order_date="2024-11-12",  # Martes
     address="Street 3"
)

print(f"Order 1 (Date: {order1.order_date}) Jueves: {order1.is_tuesday_or_wednesday()}")
print(f"Order 2 (Date: {order2.order_date}) Miércoles: {order2.is_tuesday_or_wednesday()}")
print(f"Order 3 (Date: {order3.order_date}) Martes: {order3.is_tuesday_or_wednesday()}")

print("-----------------------apply_two_for_one_promotion--------------------------------------")

order12 = PizzaOrder(
        pizzas=["Margherita", "Margherita", "Pepperoni", "Simple"],
        order_date="2024-11-14",  # Jueves
        address="Street 1"
    )
promotion = Promotion()
total_price = promotion.apply_two_for_one_promotion(json_path, order12)
print(f"Total price: {total_price}") # Total price: 32.0

order13 = PizzaOrder(
        pizzas=["Margherita", "Margherita", "Pepperoni", "Simple"],
        order_date="2024-11-20",  # miercoles
        address="Street 1"
    )
promotion = Promotion()
total_price = promotion.apply_two_for_one_promotion(json_path, order13)
print(f"Total price: {total_price}") # Total price: 24.0

order14 = PizzaOrder(
        pizzas=["Margherita"],
        order_date="2024-11-19",  # miercoles
        address="Street 1"
    )
promotion = Promotion()
total_price = promotion.apply_two_for_one_promotion(json_path, order14)
print(f"Total price: {total_price}") # Total price: 8.0


oreder15 = PizzaOrder(
    pizzas=["Pepperoni", "Pepperoni", "Hawaiian", "Margherita", "Margherita", "Simple"],  # 9 + 8 + 9 + 8 + 10
    order_date="2024-11-14",  # Jueves
    address="Street 1"
)
promotion = Promotion()
total_price = promotion.apply_two_for_one_promotion(json_path, oreder15)
print(f"Total price: {total_price}") # Total price: 44.0

print("-----------------------apply_delivery_cost_promotion--------------------------------------")

order1 = PizzaOrder(
    pizzas=["Margherita", "Pepperoni"],
    order_date="2024-11-14",  # Jueves
    address="Street 1"
)

promotion = Promotion()
delivery_cost = promotion.apply_delivery_cost_promotion(order1)
print(f"Delivery cost: ${delivery_cost:.2f}")  # Delivery cost: $0.00

order1 = PizzaOrder(
    pizzas=["Margherita", "Pepperoni"],
    order_date="2024-11-20",  # Miercoles
    address="Street 1"
)

promotion = Promotion()
delivery_cost = promotion.apply_delivery_cost_promotion(order1)
print(f"Delivery cost: ${delivery_cost:.2f}")  # Delivery cost: $0.00

order1 = PizzaOrder(
    pizzas=["Margherita", "Pepperoni"],
    order_date="2024-11-22",  # Viernes
    address="Street 1"
)

promotion = Promotion()
delivery_cost = promotion.apply_delivery_cost_promotion(order1)
print(f"Delivery cost: ${delivery_cost:.2f}")  # Delivery cost: $0.00


print("-----------------------calculate_total_price--------------------------------------")

order = PizzaOrder(
    pizzas=["Margherita", "Pepperoni", "Margherita", "Margherita", "Hawaiian"],
    order_date="2024-11-14",  # Jueves
    address="Street 1"
)


promotion = Promotion()
total_price_calculator = OrderService(json_path, additional_ingredients_path)
total_price = total_price_calculator.calculate_total_price(order, promotion)

print(f"Total price: ${total_price:.2f}") # 43


order = PizzaOrder(
    pizzas=["Margherita", "Pepperoni", "Margherita", "Margherita", "Hawaiian"],
    order_date="2024-11-20",  # miercoles
    address="Street 1"
)


promotion = Promotion()
total_price_calculator = OrderService(json_path, additional_ingredients_path)
total_price = total_price_calculator.calculate_total_price(order, promotion)

print(f"Total price: ${total_price:.2f}") # 50


order = PizzaOrder(
    pizzas=["Margherita", "Pepperoni", "Margherita", "Margherita", "Hawaiian"],
    order_date="2024-11-20",  # miercoles
    address="Street 1"
)


promotion = Promotion()
total_price_calculator = OrderService(json_path, additional_ingredients_path)
total_price = total_price_calculator.calculate_total_price(order, promotion)

print(f"Total price: ${total_price:.2f}") # 50


print("-----------------------create_order_and_save--------------------------------------")

order_data = {
    "order_number": "ORD12345",
    "order_date": "2024-11-20",  # Miércoles
    "customer_name": "Jane Doe",
    "pizzas": ["Margherita", "Pepperoni"],
    "additional_ingredients": ["pineapple"],
    "address": "123 Pizza Street"
}

file_path = "order_db.json"

order_service = OrderService(json_path, additional_ingredients_path)

order_service.create_order_and_save(file_path, order_data)