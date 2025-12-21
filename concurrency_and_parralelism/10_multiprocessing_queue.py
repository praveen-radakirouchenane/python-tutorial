from multiprocessing import Process, Queue

def your_order(queue):
    queue.put("Your order has been received!!!")


if __name__ == "__main__":

    queue = Queue()

    p = Process(target=your_order, args=(queue,))
    p.start()
    p.join()
    
    print(queue.get())