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
    "price": 5.00,
    "product": ": food"
},
{
    "name": "Banana",
    "price": 6.00,
    "product": ": food"
},
{
    "name": "Cereal",
    "price": 12.00,
    "product": ": food"
},
{
    "name": "Car_toy",
    "price": 12.00,
    "product": ": toy"
},
{
    "name": "Nerf_gun",
    "price": 25.00,
    "product": ": toy"
},
]






def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"], item["price"], item["product"])
    
shopping_cart = []
total = 0
while True:
    def choose_item():
        show_items(store)
        x = int(input("Choose an item number 0-4:"))
        print(" ")
        print(store[x])
        shopping_cart.append(store[x])

    choose_item()

    print("If you're done shopping type 'yes'")
    y = input("otherwise you can 'quit' or 'cart' or 'no:")
    if y == "yes":
        print(" ")
        total += sum(item["price"] for item in shopping_cart)
        print("shopping cart:")
        if shopping_cart:
            for item in shopping_cart:
                print(item["name"], item["price"])
                print(" ")
            else:
                print("broke empty cart")

            z = input("chechout?????????")
            if z == "yes":
                print(" ")
                print("recipt")
                print(" ")
                for item in shopping_cart:
                    print(item["name"], item["price"])
                    print(" ")
                print("your total:", float(total))
                break
            else:
                print(" ")
    elif y == "no":
                total += sum(item["price"] for item in shopping_cart)
















