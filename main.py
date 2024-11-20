import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
import logging
from models.pizza import Pizza
from models.pizza_menu import PizzaMenu
from models.pizza_order import PizzaOrder
from models.promotion import Promotion
from services.order_service import OrderService

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Ruta donde guardaremos los pedidos
ORDER_FILE_PATH = "order_db.json"

# Crear el servicio
order_service = OrderService(pizza_json_path="models/type_pizza.json", ingredients_json_path="models/ingredients_pizza.json")


# Rutas de los archivos JSON
pizza_data_path = Path('models/type_pizza.json')
ingredients_data_path = Path('models/ingredients_pizza.json')

# Route GET to fetch the pizza menu and promotions
@app.get('/menu/', tags=['Menu'])
def get_menu():
    try:
        pizza_menu = PizzaMenu(pizza_data_path=pizza_data_path,
                               ingredient_data_path=ingredients_data_path)
        pizza_menu.show_menu()
        return {"message": "Menú mostrado en la consola. Revisa la consola para más detalles."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error mostrando el menú: {e}")


@app.get('/pizza/{pizza_name}/price', tags=['Pizza'])
def get_pizza_price(pizza_name: str):
    try:
        # Obtener los nombres y precios de las pizzas
        pizza_names = Pizza.get_pizza_names_from_json(pizza_data_path)
        pizza_prices = Pizza.get_pizza_prices_from_json(pizza_data_path)

        # Normalizar el nombre de la pizza (ignorar mayúsculas/minúsculas)
        pizza_name_lower = pizza_name.lower()

        # Buscar el precio de la pizza solicitada
        if pizza_names and pizza_prices:
            pizza_names_lower = [name.lower() for name in pizza_names]
            if pizza_name_lower in pizza_names_lower:
                pizza_index = pizza_names_lower.index(pizza_name_lower)
                price = pizza_prices[pizza_index]
                return {"pizza": pizza_name, "price": price}
            else:
                raise HTTPException(status_code=404, detail="Pizza no existe.")
        else:
            raise HTTPException(status_code=404, detail="Datos de pizzas no encontrados.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el precio de la pizza: {e}")


@app.post("/create-order/", tags=['Order'])
async def create_order(order: PizzaOrder):

    order_data = order.dict()  # Convertir el objeto Pydantic a un diccionario

    # Crear la orden utilizando el método `create_order`
    order_obj = order_service.create_order(order_data)

    # Calcular el precio total usando el método `calculate_total_price`
    promotion = Promotion()  # Crear una instancia de Promotion
    total_price = order_service.calculate_total_price(order_obj, promotion)

    # Asignar el total calculado a la orden
    order_obj.total = total_price

    # Guardar la orden utilizando el método `save_order`
    order_service.save_order(ORDER_FILE_PATH, order_obj)

    # Preparar los detalles de la orden para la respuesta
    order_details = {
        "order_id": order_obj.order_number,  # Puedes usar order_number como ID o crear uno único
        "order_number": order_obj.order_number,
        "order_date": order_obj.order_date,
        "customer_name": order_obj.customer_name,
        "pizzas": order_obj.pizzas,
        "additional_ingredients": order_obj.additional_ingredients,
        "address": order_obj.address,
        "total": order_obj.total  # Esto ya es el total calculado
    }

    return {"message": "Order created successfully!", "order_details": order_details}