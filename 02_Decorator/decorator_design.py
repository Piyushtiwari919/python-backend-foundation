import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


def isPrimeNumber(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        pass


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bound: int) -> int:
        count = 0
        for i in range(upper_bound):
            if isPrimeNumber(i):
                count += 1
        return count


class AbstractDecorator(AbstractComponent):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


class BenchMarkDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        start_time = perf_counter()
        value = self._decorated.execute(upper_bound)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f"Execution of {self._decorated.__class__.__name__} took run time of {run_time:.2f} seconds"
        )
        return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    component = ConcreteComponent()
    benchmark_decorator = BenchMarkDecorator(component)
    benchmark_decorator.execute(100000)


if __name__ == "__main__":
    main()

"""
#The Flow of Code
main()

↓

Create ConcreteComponent

↓

Wrap it inside BenchmarkDecorator

↓

Call execute()

↓

BenchmarkDecorator starts timer

↓

Calls ConcreteComponent.execute()

↓

Counts prime numbers

↓

Returns count

↓

BenchmarkDecorator stops timer

↓

Print execution time

↓

Return count
"""
