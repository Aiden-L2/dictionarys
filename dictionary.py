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



shopping_cart = []
total = 0
x = 0
z = 0

while True:

    print(" ")

    def show_items(items):
        for index, item in enumerate(items):
            print(index, ":", item["name"], item["price"], item["product"])
    


    y = shopping_cart
    if y == x:
        for items in shopping_cart:
            print("shopping cart:")
            print(store[x]['name'], store[x]['price'])

    def choose_item():
        show_items(store)
        y = int(input("Choose an item number 0-4 or 'cart' or 'quit' or 'check out':"))
        print(store[y])
        shopping_cart.append(store[y])
        z = int(input("done shopping? yes or no"))
        
    choose_item()

    if y == "quit":
        break

    if y == "cart":
        print(shopping_cart)
        g = input("enter to continue")



"""     if y == "1":
        print(store[1])
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[1]['name'])
             print("item added to cart")
             print(" ")
             total += 5.50
             x = 1 """









"""     print(" ")

    if y == "check out":
        print("total cost: $",float(total), "have a great day")
        print("your purchased itesm", shopping_cart)
        break

    if y == "quit":
         break

    if y == "cart":
         print(shopping_cart)
         print("total so far $", float(total))
         s = input("press enter to keep proceeding") """
















