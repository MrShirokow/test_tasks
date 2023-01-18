import sys
import concurrent.futures

from time import perf_counter

import requests


URL = 'http://httpbin.org/delay/3'
REQUEST_COUNT = 100


def send_request(url: str):
    return requests.get(url)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=REQUEST_COUNT) as executor:
        tasks = (executor.submit(send_request, URL) for _ in range(REQUEST_COUNT))
        concurrent.futures.wait(tasks)


if __name__ == '__main__':
    start = perf_counter()
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    print(f'time: {(perf_counter() - start):.2f} seconds')
