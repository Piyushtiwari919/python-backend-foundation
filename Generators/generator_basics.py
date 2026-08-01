def square_nums(nums):
    for i in nums:
        yield i * i

my_nums = square_nums([1, 2, 3, 4, 5])

def main():
    for num in my_nums:
        print(num)

if __name__ == "__main__":
    main()
