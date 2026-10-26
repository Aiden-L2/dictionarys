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
    "product": ": food"
},
{
    "name": "Banana",
    "price": "$5.50",
    "product": ": food"
},
{
    "name": "Cereal",
    "price": "$11.79",
    "product": ": food"
},
{
    "name": "Car_toy",
    "price": "$5.69",
    "product": ": toy"
},
{
    "name": "Nerf_gun",
    "price": "$19.99",
    "product": ": toy"
},
]

def show_items(items):
        for index, item in enumerate(items):
            print(index, ":", item["name"])
    
show_items(store)

shopping_cart = []


while True:

    y = shopping_cart
    if y == 0:
        for items in shopping_cart:
            print("shopping cart:")
            print(store[0]['name'], store[0]['price'])
    y = input("Choose an item number or quit:")
    print("type shop to see your cart")
    if y == "quit":
         break
    if y == "shop":
         print(shopping_cart)
    if y == "0":
        print(store[0]['name'], store[0]['price'], store[0]['product']) 
        z = input("would you like to buy this item")
        if z == "yes":
             shopping_cart.append(store[0]['name'])
             shopping_cart.append(store[0]['price'])
             print("item added to cart")
    if y == "remove":
        print(shopping_cart) 
        print("what do you want to remove from your list")







"""     elif y == "1":
        print(store[1]['name'], store[1]['price'], store[1]['product'])
    elif y == "2":
        print(store[2]['name'], store[2]['price'], store[2]['product'])
    elif y == "3":
        print(store[3]['name'], store[3]['price'], store[3]['product'])
    elif y == "4":
        print(store[4]['name'], store[4]['price'], store[4]['product']) """










"""     for stores in store:
        print(stores['name'], stores['price']) """




"""     "name": "",
    "price": "",
    "type": "" """

