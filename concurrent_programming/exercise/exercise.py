# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Retrieve data from multiple URLs concurrently using asyncio
# Implement a function named retrieve_data to retrieve data from each of the provided URLs
# concurrently using asyncio and the fetch function.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import asyncio
from time import perf_counter, sleep

async def fetch(url: str) -> str:
    # Simulate network delay
    # await asyncio.sleep(2)
    return f"Data from {url}"


# TODO: Implement the retrieve_data function
async def retrieve_data(urls: list[str]) -> list[str]:
    tasks = [fetch(url) for url in urls]
    data = await asyncio.gather(*tasks)
    return data

async def main() -> None:
    time_before = perf_counter()
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]
    data = await retrieve_data(urls)
    print(data)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")
    
    # TODO: Use the retrieve_data function to retrieve data from the provided URLs concurrently

def synchronous_fetch(url: str):
    # sleep(2)
    return f"Data from {url}"

def synchronouse_retrieve_data(urls: list[str])-> list[str]:
    return [synchronous_fetch(url) for url in urls]

def synchronous_main():
    time_before = perf_counter()
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]
    data = synchronouse_retrieve_data(urls)
    print(data)
    print(f"Total time (synchronous): {perf_counter() - time_before}")
    
if __name__ == "__main__":
    asyncio.run(main())
    synchronous_main()
