import random
import time
from functools import wraps


def retry_with_jitter(max_attempts=5, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempts == max_attempts - 1:
                        raise e

                    # Calculate exponential delay
                    exp_delay = base_delay * (2**attempts)

                    # Add Jitter: Random float between 0 and 1
                    jitter = random.uniform(0, 1)
                    final_delay = exp_delay + jitter

                    print(f"⏳ Backoff: Waiting {final_delay:.2f}s...")
                    time.sleep(final_delay)
                    attempts += 1

        return wrapper

    return decorator


@retry_with_jitter(max_attempts=4)
def call_llm_api():
    print("\nInitiating API Request...")
    raise ConnectionError("HTTP 429: Too Many Requests")


try:
    call_llm_api()
except Exception as e:
    print(f"Final Failure: {e}")


"""
The theory:
In a true production environment, exponential backoff has a hidden flaw called the "Thundering Herd" problem.

Imagine 500 Node.js/Express backend servers (like the ones use in your MERN stack) all hit the Anthropic API at the exact same second, and the API goes down.
All 500 servers will wait exactly 1 second, then hit the API simultaneously. It fails.
All 500 servers will wait exactly 2 seconds, then hit the API simultaneously. It fails.

Even though they are backing off, they are doing it in perfect lockstep, creating massive, synchronized spikes of traffic that act like a hammer.

The Solution: Jitter (Randomness)
To break the synchronization, we add a random float number (Jitter) to the delay. This scatters the retries across a time window.

If we add a random value between 0 and 1 second to a 4-second delay, Server A might wait 4.1s, Server B waits 4.7s, and Server C waits 4.2s. The load is smoothly distributed.
"""

"""The answer: I implement an exponential backoff strategy with randomized jitter to prevent thundering herd spikes on the external server, usually wrapped in a decorator to keep my business logic clean"""
