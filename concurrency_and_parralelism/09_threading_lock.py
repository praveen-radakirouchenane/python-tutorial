import threading


count = 0
lock = threading.Lock() #Thread safe and it will make sure won't override memory at the same time 

#with lock
def counter(itr):
    print(f"Iteration# {itr}")
    global count
    for i in range(2):
        with lock:
            count+=1
    print(f"Counter value inside function # {count}")

## without lock 
# def counter(itr):
#     print(f"Iteration# {itr}")
#     global count
#     for i in range(20):
#         count+=1
#     print(f"Counter value inside function # {count}")

threads = [threading.Thread(target=counter, args=(i,)) for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]


print(f"Total counter value is {count}")