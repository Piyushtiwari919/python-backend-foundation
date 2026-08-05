import asyncio
from concurrent.futures import ProcessPoolExecutor


def chunk_massive_document() -> int:
    """A synchronous CPU-bound task simulating heavy text processing"""
    print("[CPU] Starting heavy computation (locking the CPU)...")

    result: int = sum(i * i for i in range(30000000))

    print("[CPU] Finished heavy computation!")
    return result


async def serve_user(id: int, cpuTask: bool) -> None:
    print(f"User: {id} requested")
    if cpuTask:
        loop = asyncio.get_running_loop()
        executor = ProcessPoolExecutor(4)
        res = await loop.run_in_executor(executor, chunk_massive_document)
        print(f"The output of User: {id} task is {res}")
        print(f"User: {id} request completed")
        executor.shutdown()
    else:
        print(f"User: {id} requested a fast profile load.")

        await asyncio.sleep(0.1)

        print(f"User: {id} Profile load complete.")


async def main():
    print("--- Server Started ---")
    try:
        await asyncio.gather(serve_user(1, True), serve_user(2, False))
    except Exception as e:
        print(f"Exception occured: {e}")


if __name__ == "__main__":
    asyncio.run(main())
