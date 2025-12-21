import time
import threading

def greetings():
    while True:
        print("I am sleeping now")
        time.sleep(2)

threading.Thread(target=greetings).start() #this thread will continuosly run until hard kill(ctrl+C) the main thread

print("I am the main thread")