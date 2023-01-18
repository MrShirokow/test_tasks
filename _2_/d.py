import sys

from time import perf_counter

import asyncio
import aiohttp

from aiohttp.client_exceptions import InvalidURL


URL = 'http://httpbin.org/delay/3'
REQUEST_COUNT = 100


async def send_request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            await response.text()


async def main():
    tasks = []
    for _ in range(REQUEST_COUNT):
        tasks.append(asyncio.create_task(send_request(URL)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = perf_counter()
    try:
        asyncio.run(main())
    except InvalidURL as e:
        print(f'invalid URL: {e}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    print(f'time: {(perf_counter() - start):.2f} seconds')
