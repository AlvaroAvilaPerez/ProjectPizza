# Pizza Order API

This is a FastAPI application for handling pizza orders. You can create and manage pizza orders with this API. Below are the steps to set up, run, and interact with the API.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (preferably 3.8 or higher)
- Postman (for testing the API)

## Installation

1. Clone the repository or download the project files.
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   
## Activate the virtual environment:

On Windows:

```bash
.\.venv\Scripts\activate
```
On macOS/Linux:

```bash
source .venv/bin/activate
```
## Install the required dependencies:

```bash
pip install -r requirements.txt
```

##  Running the Application
To run the FastAPI application locally, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server at http://127.0.0.1:8000.

## Testing with Postman
1. Open Postman on your desktop.
2. Create a new POST request with the following details:
URL: http://127.0.0.1:8000/order/
Method: POST
Body: Use the following JSON in the body:

```bash
{
  "id": 1,
  "order_number": "ORD12345",
  "order_date": "2024-11-20",
  "customer_name": "Jane Doe",
  "pizzas": [
    "Margherita",
    "Pepperoni"
  ],
  "additional_ingredients": [
    "pineapple"
  ],
  "address": "123 Pizza Street",
  "total": 26.0
}
```