import time
import asyncio
import httpx
from functools import wraps


# def timerdecorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f"{func.__name__} ran in {(end_time - start_time):.4f} time")
#         return result

#     return wrapper


async def fetch_data(client, service_name):
    try:
        print(f"Started fetching data from {service_name}")
        await asyncio.sleep(2)
        print(f"Finished fetching {service_name} data")

        return {"service": service_name, "status": "online"}

    except Exception as e:
        print(f"Error: {e}")


# @timerdecorator
async def main():
    # m-1
    # async with httpx.AsyncClient() as client:
    #     tasks = [
    #         fetch_data(client, "Temperature Data"),
    #         fetch_data(client, "Wind Data"),
    #         fetch_data(client, "Rain Data"),
    #     ]

    #     results = await asyncio.gather(*tasks)

    # m-2
    client = httpx.AsyncClient()
    try:
        task1 = asyncio.create_task(fetch_data(client, "Temperature Data"))
        task2 = asyncio.create_task(fetch_data(client, "Wind Data"))
        task3 = asyncio.create_task(fetch_data(client, "Rain Data"))
        res1 = await task1
        res2 = await task2
        res3 = await task3
    finally:
        # Explicitly close the connection pool to prevent socket leaks
        await client.aclose()

    print(res1, res2, res3)


if __name__ == "__main__":
    asyncio.run(main())
