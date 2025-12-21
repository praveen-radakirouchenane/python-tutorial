import asyncio

async def gretting(name):
    print(f"Hi {name}, How are you?")
    await asyncio.sleep(2)
    print(f"See you {name}, nice to meet you!!!")


async def main():
    print("Calling Greeting function!")
    await asyncio.gather(
        gretting("Praveen"),
        gretting("Kumar"),
        gretting("PK")
    )
    print("Exiting from Greeting function!")


asyncio.run(main())