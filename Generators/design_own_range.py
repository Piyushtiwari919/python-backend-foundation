class OwnRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return OwnRangeIterator(self)


class OwnRangeIterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start
        self.iterable.start += 1
        return current


def range_test():
    for i in OwnRange(1, 11):
        print(i)


def main() -> None:
    range_test()


if __name__ == "__main__":
    main()
