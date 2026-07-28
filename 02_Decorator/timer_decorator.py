import time


def timerdecorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper


@timerdecorator
def ex_func(n):
    time.sleep(n)


if __name__ == "__main__":
    ex_func(3)
