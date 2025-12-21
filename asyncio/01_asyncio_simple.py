import asyncio

async def greeting():
    print("Hello world!!!")
    await asyncio.sleep(2)
    print("See you world!!!")

asyncio.run(greeting())
