""" vac = {
    "name": "Dyson V15 Cordless Vacuum",
    "price": 699.99,
    "department": "Appliances",
    "description": "High-powered cordless vacuum with laser dust detection."
}
print(vac["name"], vac["price"]) """

""" best_buy_items = [
    {
        "name": "Samsung 55\" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
    },
    {
        "name": "Sony Noise Cancelling Headphones",
        "price": 299.99,
        "department": "Audio",
        "description": "Wireless over-ear headphones with industry-leading noise cancellation."
    },
    {
        "name": "Apple iPhone 15",
        "price": 999.99,
        "department": "Mobile Phones",
        "description": "Latest Apple smartphone with A17 chip and advanced camera system."
    }
]

def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

def choose_item():
    show_items(best_buy_items)
    x = int(input("Which item number do you want to buy? "))
    print(best_buy_items[x])

choose_item() """

store = [
{
    "name": "Apple",
    "price": "$4.99",
    "type": "food"
},
{
    "name": "Banana",
    "price": "$5.50",
    "type": "food"
},
{
    "name": "Cereal",
    "price": "$11.79",
    "type": "food"
},
{
    "name": "Car_toy",
    "price": "$5.69",
    "type": "toy"
},
{
    "name": "Nerf_gun",
    "price": "$19.99",
    "type": "toy"
},
]

print("What would you like to buy?")

def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

show_items(store)


y = input("")





"""     for stores in store:
        print(stores['name'], stores['price']) """




"""     "name": "",
    "price": "",
    "type": "" """