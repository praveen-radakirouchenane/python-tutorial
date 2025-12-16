class ItemNotAvailable(Exception): pass 

def your_order(item, quantity):
    menu = {"noodles":20, "pasta":30}

    try:
        if item not in menu:
            raise ItemNotAvailable("Your ordered item is not available")
        if not isinstance(quantity, int):
            raise TypeError("Please enter a quantiy in numbers")
    
        cost = menu[item] * quantity
        print(f"Your ordered item is {item}, and total quantity is {quantity}, and the total price is {cost}")

    except Exception as e:
        print('Error: ',e)
    
    finally:
        print('Thank you for visiting us!!!')


your_order('curry',1)
your_order('pasta','10')
your_order('pasta',20)
        