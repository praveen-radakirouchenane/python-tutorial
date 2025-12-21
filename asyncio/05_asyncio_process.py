import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def your_order(name):
    print(f"You order: {name}")
    time.sleep(3) # Blocking operation
    return f"Your {name} is ready!"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, your_order, "coffee") #your_order function will run seperately in different thread which doesn't block the main thread
        print(result)

if __name__ == "__main__":
    asyncio.run(main())