import math
from collections.abc import Iterator, Sequence
from concurrent.futures import ProcessPoolExecutor


def isPrime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


numbers: Sequence[int] = [112272535095293, 112582705942171, 115280095190773]


def multi_processing() -> None:
    with ProcessPoolExecutor() as executor:
        results: Iterator[int] = executor.map(isPrime, numbers)
        for number, prime in zip(numbers, results):
            print(f"{number} is prime: {prime}")


if __name__ == "__main__":
    multi_processing()
