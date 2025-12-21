from multiprocessing import Process, Value

def order_count(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value+=1 # object for this memory is shared across all the processes

if __name__ == "__main__":
    counter = Value("i",0)
    processes = [Process(target=order_count, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Total counter value is {counter.value}")