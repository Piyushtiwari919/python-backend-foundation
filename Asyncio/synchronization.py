import asyncio

# Lock

shared_resources = 0

lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resources
    async with lock:
        # Critical Section starts
        print(f"Resource before Modification: {shared_resources} ")
        shared_resources += 1
        await asyncio.sleep(1)
        print(f"Resource After Modification: {shared_resources} ")
        # Critical Section ends


# async def main() -> None:
#     await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

# Semaphore


async def access_resource(semaphore, id):
    async with semaphore:
        # Access concurrently
        print(f"Accessing resource: {id}")
        await asyncio.sleep(1)
        print(f"Releasing Resource: {id}")


async def main() -> None:
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


if __name__ == "__main__":
    asyncio.run(main())
