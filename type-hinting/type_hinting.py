import random
from typing import NewType
from dataclasses import dataclass

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


# class User(TypedDict):
#     firstName: str
#     lastName: str
#     email: str
#     age: int | None
#     fav_color: RGB | None


@dataclass
class User:
    firstName: str
    lastName: str
    email: str
    age: int | None
    fav_color: RGB | None


def createUser(
    firstName: str, lastName: str, age: int | None = None, fav_color: RGB | None = None
) -> User:
    email: str = f"{firstName.lower()}.{lastName.lower()}@python.mail.com"
    return User(
        firstName=firstName,
        lastName=lastName,
        email=email,
        age=age,
        fav_color=fav_color,
    )

    # return {
    #     "firstName": firstName,
    #     "lastName": lastName,
    #     "email": email,
    #     "age": age,
    #     "fav_color": fav_color,
    # }

#Generic Type
def random_choice[T](items: list[T]) -> T:
    return random.choice(items)


def type_hinting() -> None:
    #Creating User
    user1 = createUser("John", "Doe", 27, RGB((101, 212, 211)))
    user2 = createUser("Shawn", "Dev", 27, RGB((150, 112, 191)))

    #Accessing Random User
    user = random_choice([user1, user2])
    print(user)


if __name__ == "__main__":
    type_hinting()
