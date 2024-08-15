import json

try:
    with open('fruitsDictionary.json') as filehandler:
        data = json.load(filehandler)
    for product in data:
        print(f"Product: {product["product"]}")
        print(f"Quantity: {product["quantity"]}")
        print(f"Price: {product["price"]}")
        print("="*25)
except Exception as e:
    print("Something went wrong:", e)