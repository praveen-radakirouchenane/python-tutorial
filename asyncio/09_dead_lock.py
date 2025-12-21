import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def my_task_1():
    with lock_1:
        print("My Task 1 has acquired the Lock 1")
        with lock_2:
             print("My Task 1 has acquired the Lock 2")

def my_task_2():
    with lock_2:
        print("My Task 2 has acquired the Lock 2")
        with lock_1:
             print("My Task 2 has acquired the Lock 1")


thread_1 = threading.Thread(target=my_task_1)
thread_2 = threading.Thread(target=my_task_2)

thread_1.start()
thread_2.start()