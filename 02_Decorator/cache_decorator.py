import time


def cache(func):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def dBCall(a, b):
    time.sleep(5)
    return a + b


if __name__ == "__main__":
    print(dBCall(2, 3))
    print(dBCall(2, 3))
