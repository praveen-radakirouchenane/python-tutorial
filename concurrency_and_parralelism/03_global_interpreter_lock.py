import threading
import time

def your_order():
    print(f"Starting order for {threading.current_thread().name}")
    count =0 #both threads tries to access the same object in the memory but Mutex will allow one by one  
    for _ in range(100_000_000):
        count +=1
    print(f"Finishing order for {threading.current_thread().name}") 


start = time.time()

order_1 = threading.Thread(target=your_order, name="Praveen")
order_2 = threading.Thread(target=your_order, name="Kumar")

order_1.start()
order_2.start()

order_1.join()
order_2.join()

end = time.time()

print(f"Total time taken to finish the orders: {end-start:.2f} seconds")