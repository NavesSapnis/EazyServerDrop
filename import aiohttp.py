import aiohttp
import asyncio

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def make_requests(url, count):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(count):
            tasks.append(fetch(url, session))
            print("Добавил: "+str(i)+" запросов")
        responses = await asyncio.gather(*tasks)
        print("Выполнил все запросы вкусно нахуй")
        return len(responses)

url = 'https://www.kbp.by/'
count = 100000

loop = asyncio.get_event_loop()
num_requests = loop.run_until_complete(make_requests(url, count))
print(f"Number of requests made: {num_requests}")