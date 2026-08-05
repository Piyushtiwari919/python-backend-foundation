import asyncio


async def failing_task():
    print("Failing task: Starting...")
    await asyncio.sleep(1)
    print("Failing task: Crashing now!")
    raise ValueError("Database connection lost.")


async def safe_task():
    print("Safe task: Starting...")
    try:
        await asyncio.sleep(3)
        print("Safe task: Finished successfully.")
    except asyncio.CancelledError:
        # The TaskGroup sends this specific error to abort the task
        print("Safe task: I was cleanly cancelled by the TaskGroup!")


async def main_taskgroup():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(failing_task())
            tg.create_task(safe_task())

    except Exception as e:  # noqa: BLE001, F841
        print("Main caught error from TaskGroup.")
        # TaskGroup wraps errors in an **ExceptionGroup in case multiple tasks fail at once


asyncio.run(main_taskgroup())
