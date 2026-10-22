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
    "type": ": food"
},
{
    "name": "Banana",
    "price": "$5.50",
    "type": ": food"
},
{
    "name": "Cereal",
    "price": "$11.79",
    "type": ": food"
},
{
    "name": "Car_toy",
    "price": "$5.69",
    "type": ": toy"
},
{
    "name": "Nerf_gun",
    "price": "$19.99",
    "type": ": toy"
},
]

""" def show_items(items):
        for index, item in enumerate(items):
            print(index, ":", item["name"])
    
show_items(store)

while True:
    print("What would you like to buy?")

    y = int(input(""))
    if int(y) == "0":
        print(store[0]['name'], store[0]['price'], store[0]['type'])
        
    elif int(y) == "1":
        print(store[1]['name'], store[1]['price'], store[1]['type'])
    elif int(y) == "2":
        print(store[2]['name'], store[2]['price'], store[2]['type'])
    elif int(y) == "3":
        print(store[3]['name'], store[3]['price'], store[3]['type'])
    elif int(y) == "4":
        print(store[4]['name'], store[4]['price'], store[4]['type'])





 """




"""     for stores in store:
        print(stores['name'], stores['price']) """




"""     "name": "",
    "price": "",
    "type": "" """

def slot_machine(q,slot_1,slot_2,slot_3):
    plays = 0

    while True:
        if q == 1:
            q = q - 1
            slot_1 + 1 == slot_1
            plays + 1 == plays
        elif slot_1 % 35 == 0:
            q = q + 30
        if q == 1:
            q = q - 1
            slot_2 + 1 == slot_2
            plays + 1 == plays
        elif slot_2 % 100 == 0:
            q = q + 60
        if q == 1:
            q = q - 1
            slot_3 + 1 == slot_3
            plays + 1 == plays
        elif slot_3 % 10 == 0:
            q = q + 9
        if q == 0:
            print("Martha plays", str(plays), "before going broke")
            break
slot_machine(2,3,10,4)

"""     plays = 0
    q = 48
    slot_1 = 3 
    slot_2 = 10
    slot_3 = 4 """