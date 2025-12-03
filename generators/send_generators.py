def welcome_to_restaurant():
    print("Welcome to the Thai Restaurant!!!")
    dish = yield

    while True:
        print(f"You ordered {dish}")
        dish = yield


your_order = welcome_to_restaurant()
next(your_order)
your_order.send("Red curry")   
your_order.send("Green curry")    