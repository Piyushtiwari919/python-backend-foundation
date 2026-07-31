import logging
from math import sqrt
from collections.abc import Callable
from time import perf_counter
from typing import Any
from functools import cache, wraps, partial

logger = logging.getLogger("my_app")


def isPrimeNumber(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logger.info(
            f"Execution of {func.__name__} took run time of {run_time:.2f} seconds"
        )
        return value

    return wrapper


def with_logging(
    func: Callable[..., Any], logger: logging.Logger
) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logger.info(f"finished calling {func.__name__}")
        return value

    return wrapper


with_default_logging = partial(with_logging, logger=logger)


@with_default_logging
@benchmark
def count_prime(upper_bound: int) -> int:
    count = 0
    for i in range(upper_bound):
        if isPrimeNumber(i):
            count += 1
    return count


# Next Calls become faster(Caching)
@cache
def _factorial(n: int) -> int:
    if n <= 1:
        return n
    return n * _factorial(n - 1)


@benchmark
def factorial(n: int) -> int:
    return _factorial(n)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime(100000)
    logger.info(f"The number of primes are: {value}")
    factorial(500)
    factorial(600)


if __name__ == "__main__":
    main()
