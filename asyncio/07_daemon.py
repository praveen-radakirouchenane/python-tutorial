import time
import threading

def greetings():
    while True:
        print("I am sleeping now")
        time.sleep(2)

threading.Thread(target=greetings, daemon=True).start() #this is the thread which will run in the background continuosly until the life of main thread

print("I am the main thread")