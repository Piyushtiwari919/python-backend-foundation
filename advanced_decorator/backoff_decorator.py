import random
import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def backoff_retry(max_attempts: int = 3, base_delay: int = 1) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while max_attempts > attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_attempts} failed: {e}")
                    if attempts == max_attempts:
                        print(f"Max retries reached failed permanentely")
                        raise e
                    delay = base_delay * (2**attempts)
                    print(f"waiting {delay} seconds before retrying")
                    time.sleep(delay)
        return wrapper

    return decorator


@backoff_retry(max_attempts=4, base_delay=1)
def call_openai_api(prompt):
    print(f"\nSending prompt to OpenAI: '{prompt}'")

    if random.random() < 0.8:
        raise ConnectionError("OpenAI Servers are overloaded (HTTP 502)")

    return "AI Response: The capital of France is Paris."


def main():
    final_result = call_openai_api("What is the capital of France?")
    print(final_result)


if __name__ == "__main__":
    main()
