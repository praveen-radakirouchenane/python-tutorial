from multiprocessing import Process
import time

def go_to_shop(name):
    print(f"On the way to {name} shop")
    time.sleep(3)
    print(f"Completed shopping in {name}")
 

if __name__ == "__main__":
    shopping = [
        Process(target=go_to_shop, args=(f"Woolies #{i+1}",))
        for i in range(3)
    ]

    # start all Process
    for p in shopping:
        p.start()

    # Wait for all Process to complete
    for p in shopping:
        p.join()

    print("Shopping over!!!")


