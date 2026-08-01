def for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

def main() -> None:
    l = [1, 2, 3, 4]
    for_loop(l)


if __name__ == "__main__":
    main()
