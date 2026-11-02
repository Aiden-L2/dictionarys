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

    show_items(store)

    y = shopping_cart
    if y == x:
        for items in shopping_cart:
            print("shopping cart:")
            print(store[x]['name'], store[x]['price'])

    y = input("Choose an ietm number 0-4 or 'cart' or 'quit' or 'check out':")

    print(" ")

    if z == "quit":
        break



    print(" ")

    if y == "check out":
        print("total cost: $",float(total), "have a great day")

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
                    print(store[3])
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
                    print(store[4])
                break

