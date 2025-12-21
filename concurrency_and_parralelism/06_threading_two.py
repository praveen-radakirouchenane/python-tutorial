import threading
import time

def your_order(type_, wait_time):
    print(f"Your ordered {type_}, and started preparing")
    time.sleep(wait_time)
    print(f"Your {type_} is ready")



start = time.time()

your_order_thread_one = threading.Thread(target=your_order, args=("coffee",2))
your_order_thread_two = threading.Thread(target=your_order, args=("Juice",4))


your_order_thread_one.start()
your_order_thread_two.start()

your_order_thread_one.join()
your_order_thread_two.join()

end = time.time()

print(f"Total time taken for your order is {end-start:.2f} seconds")