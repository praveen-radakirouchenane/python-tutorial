def your_order(item, quantity):
    try:
        price = {"bread":7}[item]
        cost = price * quantity 
        print("Your Total price is :",cost)
    except KeyError:
        print('Not a valid item to order')
    except TypeError:
        print("Not a valid quantity to order")


#your_order("bread",7)
#your_order("banana",7)
#your_order("bread","7") // need to fix this to throw Type error