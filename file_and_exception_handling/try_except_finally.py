def your_order(order):
    try:
        print(f"Your order is {order}")
        if(order == "coffee"):
            raise ValueError(f"Sorry! We don't serve {order} here")
    except ValueError as e:
        print("Er :",e)
    else: 
        print(f"Thanks for ordering {order}")
    finally:
        print("See you soon!")


your_order("Red curry")
your_order('coffee')