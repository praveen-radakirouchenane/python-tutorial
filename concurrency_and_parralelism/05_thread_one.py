import threading
import time

def your_order(type_):
    print(f"Your ordered {type_}, and started preparing")
    time.sleep(2)
    print(f"Your {type_} is ready")

def delivery_status():
    print(f"On the way to pickup")
    time.sleep(3)
    print("Pickup is completed")


start = time.time()

your_order_thread = threading.Thread(target=your_order, args=("coffee",))
delivery_status_thread = threading.Thread(target=delivery_status)

your_order_thread.start()
delivery_status_thread.start()

your_order_thread.join()
delivery_status_thread.join()

end = time.time()

print(f"Total time taken for your order is {end-start:.2f} seconds")