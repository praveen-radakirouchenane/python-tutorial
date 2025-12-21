import aiohttp
import asyncio

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"For the fetched {url} the response status code is: {response.status}")

async def main():
    urls = ["http://httpbin.org/delay/2"]*3 
    async with aiohttp.ClientSession() as session:
        tasks =  [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())