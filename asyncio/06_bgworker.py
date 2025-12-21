import threading
import time
import asyncio

def backgroud_task():
    while True:
        time.sleep(1)
        print("System health check")

async def async_background_task():
    await asyncio.sleep(5)
    print("Checking asyncio health check")


threading.Thread(target=backgroud_task, daemon=True).start()

asyncio.run(async_background_task())