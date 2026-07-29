def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(
            f"Calling with {func.__name__} with args {args_value} and kwargs {kwargs_value}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name: str, greeting: str = "Hello"):
    print(f"{greeting} {name} ?")


if __name__ == "__main__":
    # function call
    greet("John", greeting="How are you")
