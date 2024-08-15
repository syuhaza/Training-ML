import pickle

myvar = [
    { 'product': "Television", 'quantity': 10, 'price': 1455.55 },
    { 'product': "Computer", 'quantity': 20, 'price': 3285.25 }
]

try:
    with open('fruitsdictionary.bin', 'wb') as filehandler:
        pickle.dump(myvar, filehandler)
except Exception as e:
    print("Something went wrong:", e)

try:
    filehandler = open('fruitsdictionary.bin', 'rb')
    data = pickle.load(filehandler)
    for product in data:
        print(f"Product: {product["product"]}")
        print(f"Quantity: {product["quantity"]}")
        print(f"Price: {product["price"]}")
        print("="*25)
except Exception as e:
    print("Something went wrong:", e)
