from concurrent.futures import ProcessPoolExecutor
from fastapi import FastAPI
import asyncio

app = FastAPI()

# 1. Create a pool of background processes (usually equal to your CPU cores)
process_pool = ProcessPoolExecutor(max_workers=4)


def calculate_embeddings_sync(text):
    """The heavy CPU math. This will run on a completely separate CPU core."""
    print(f"Background Process: Calculating embeddings for '{text}'...")
    total = sum(i * i for i in range(30_000_000))
    return total


@app.post("/embed")
async def generate_embedding(text: str):
    # 2. Get the current active Event Loop
    loop = asyncio.get_running_loop()

    # 3. Offload the synchronous math to the Process Pool
    # We 'await' it, meaning the Event Loop pauses this specific request
    # and goes to serve other FastAPI users while the background core does the math.
    result = await loop.run_in_executor(
        process_pool,
        calculate_embeddings_sync,
        text,
    )

    return {"embedding": result}


async def main():
    await generate_embedding("Paris is the capital of France")


if __name__ == "__main__":
    asyncio.run(main())
