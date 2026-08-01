from collections.abc import Callable
from functools import wraps
from typing import Any
import random
import time


try:
    from memory_profiler import profile  # type: ignore
except Exception:

    def profile(func: Callable[..., Any]) -> Callable[..., Any]:
        return func


names_list = ["John", "George", "Scholey", "Jitesh", "Dhoni"]
majors_list = ["CS", "AI", "M&C", "ELC", "CS"]


# Timer Decorator
def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Time consumed in running {func.__name__}: {run_time:.4f}")
        return result

    return wrapper


@profile
@timer
def people_list(num_people: int) -> list[dict]:
    result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names_list),
            "major": random.choice(majors_list),
        }
        result.append(person)
    return result


@profile
@timer
def people_generator(num_people) -> Any:
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names_list),
            "major": random.choice(majors_list),
        }

        yield person


def main() -> None:
    # Time and Memory Consumption -> High
    people_list(1000000)

    # Time and Memory Consumption -> Less
    people_generator(1000000)


if __name__ == "__main__":
    main()
