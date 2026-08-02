import time
from functools import wraps


def timerdecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} ran in {(end_time - start_time):.4f} time")
        return result

    return wrapper


def fetch_data(service_name):
    try:
        print(f"Starting sync fetch for {service_name}...")
        time.sleep(2)  # Blocks the entire Python process
        return {"service": service_name, "status": "online"}
    except Exception as e:  # noqa: BLE001
        print("Error:", e)
        return


@timerdecorator
def main():
    # Blocking Request for I/O ( CPU IS IDLE )
    fetch_data("Temperature API")
    fetch_data("Wind API")
    fetch_data("Rain API")


if __name__ == "__main__":
    main()
