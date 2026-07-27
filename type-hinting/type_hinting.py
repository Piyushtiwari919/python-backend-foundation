import random
from dataclasses import dataclass
from typing import NewType, TypedDict

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
    fav_color: RGB | None = None


class Student(TypedDict):
    name: str
    age: int


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


# Generic Type
def random_choice[T](items: list[T]) -> T:
    return random.choice(items)


def getAge(students: dict[str, Student]) -> list[int]:
    ageList: list[int] = []
    for key in students:
        ageList.append(students[key]["age"])
    return ageList


def type_hinting() -> None:
    # Creating User
    user1 = createUser("John", "Doe", 27, RGB((101, 212, 211)))
    user2 = createUser("Shawn", "Dev", 27, RGB((150, 112, 191)))

    # Accessing Random User
    user = random_choice([user1, user2])

    # Accessing Nested Dictionary
    ageList = getAge(
        {
            "studentA": {"name": "Akash", "age": 20},
            "studentB": {"name": "Ayush", "age": 19},
            "studentC": {"name": "Ben", "age": 21},
        }
    )
    print(ageList)


if __name__ == "__main__":
    type_hinting()
