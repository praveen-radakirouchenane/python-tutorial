import threading
import time

def go_to_shop():
    for i in range(1,4):
        print(f"On the way to shop: {i}")
        time.sleep(5) #play around with this 

def buy_grocery():
    for i in range(1,4):
        print(f"Started buying groceries: {i}")
        time.sleep(1) #play around with this 

go_to_shop_thread = threading.Thread(target=go_to_shop)
buy_grocery_thread = threading.Thread(target=buy_grocery)

go_to_shop_thread.start()
buy_grocery_thread.start()

#Join the threads
go_to_shop_thread.join()
buy_grocery_thread.join()
