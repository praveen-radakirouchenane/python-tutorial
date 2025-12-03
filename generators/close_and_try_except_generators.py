def order():
    try: 
        while True:
            yield "I am inside try block"
    except: 
        print("I am inside except block")

your_order = order()
print(next(your_order))
your_order.close() # cleanup
   