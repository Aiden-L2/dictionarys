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


while True:

    print(" ")

    def show_items(items):
        for index, item in enumerate(items):
            print(index, ":", item["name"], item["price"], item["product"])
    
    show_items(store)

    y = shopping_cart
    if y == x:
        for items in shopping_cart:
            print("shopping cart:")
            print(store[x]['name'], store[x]['price'])
            
    y = input("Choose an item number 0-4 or 'cart' or 'quit' or 'check out':")

    print(" ")

    if y == "check out":
        print("total cost: $",float(total), "have a great day")
        print("your purchased itesm", shopping_cart)
        break

    if y == "quit":
         break

    if y == "cart":
         print(shopping_cart)
         print("total so far $", float(total))
         s = input("press enter to keep proceeding")

    if y == "0":
        print(store[0]) 
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[0]['name'])
             shopping_cart.append(store[0]['price'])
             print("item added to cart")
             print(" ")
             total += 4.99
             x = 0
             y = input("would you like to continue?")
             if y == "no":   
                print("total cost: $",float(total), "have a great day") 
                for items in shopping_cart:
                    print(store[0]['name'], store[0]['price'])
                break

    elif y == "1":
        print(store[1])
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[1]['name'])
             shopping_cart.append(store[1]['price'])
             print("item added to cart")
             print(" ")
             total += 5.50
             x = 1
             y = input("would you like to continue?")
             if y == "no":
                print("total cost: $",float(total), "have a great day") 
                for items in shopping_cart:
                    print(store[1]['name'], store[1]['price'])
                break
             
    elif y == "2":
        print(store[2])
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[2]['name'])
             shopping_cart.append(store[2]['price'])
             print("item added to cart")
             print(" ")
             total += 11.79
             x = 2
             y = input("would you like to continue?")
             if y == "no":
                print("total cost: $",float(total), "have a great day") 
                for items in shopping_cart:
                    print(store[2]['name'], store[2]['price'])
                break

    elif y == "3":
        print(store[3])
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[3]['name'])
             shopping_cart.append(store[3]['price'])
             print("item added to cart")
             print(" ")
             total += 5.69
             x = 3
             y = input("would you like to continue?")
             if y == "no":
                print("total cost: $",float(total), "have a great day") 
                for items in shopping_cart:
                    print(store[3]['name'], store[3]['price'])
                break

    elif y == "4":
        print(store[4])
        z = input("would you like to buy this item:")
        if z == "yes":
             shopping_cart.append(store[4]['name'])
             shopping_cart.append(store[4]['price'])
             print("item added to cart")
             print(" ")
             total += 19.99
             x = 4
             y = input("would you like to continue?")
             if y == "no":
                print("total cost: $",float(total), "have a great day") 
                for items in shopping_cart:
                    print(store[4]['name'], store[4]['price'])
                break
















