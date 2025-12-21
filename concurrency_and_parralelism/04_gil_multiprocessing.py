from multiprocessing import Process
import time 

def your_order():
    print(f"Preparing your order")
    count=0 # Here, there is no mutex concept where both processes access the same 'count' object in parrallel so be careful while choosing this method
    for _ in range(100_000_000):
        count+=1
    print(f"Finishing your order")


if __name__ == "__main__":
    start = time.time()

    process_1 = Process(target=your_order)
    process_2 = Process(target=your_order)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    end = time.time()

    print(f"Total time taken to finish the order is {end-start:.2f} seconds")

