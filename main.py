# l-1
# from collections.abc import Iterable

# def calculate_discounts(items:Iterable[float], discount:float)->float:
#     return sum(items)-(1-discount)

# l-2


def createUser(firstName: str, lastName: str, age: int) -> dict:
    email = f"{firstName.lower()}.{lastName.lower()}@python.mail.com"
    return {"firstName": firstName, "lastName": lastName, "email": email, "age": age}


def main() -> None:
    # l-1
    # items= [10.0,20.0,30.0,40.0,50.0]
    # discount = 0.2
    # # total = calculate_discounts(items,discount)
    # total = calculate_discounts((x*10 for x in items),discount)
    # print(total)

    # l-2

    user1 = createUser("John", "Doe", 25)
    print(user1)

    # print("Hello from type-hinting!")


if __name__ == "__main__":
    main()
