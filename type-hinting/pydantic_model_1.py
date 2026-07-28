import time
from datetime import UTC, datetime
from typing import Literal, Annotated
from uuid import UUID, uuid4
from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    ValidationError,
    EmailStr,
    HttpUrl,
    SecretStr,
    computed_field,
    field_validator,
    model_validator,
    ValidationInfo,
)


class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    uid: UUID = Field(alias="id", default_factory=uuid4)
    username: Annotated[str, Field(min_length=6, max_length=20)]
    email: EmailStr
    password: SecretStr
    firstName: str = ""
    lastName: str = ""
    followerCount: int = 0
    website: HttpUrl | None = None
    verifiedAt: datetime | None = None
    isVerified: bool | None = False
    age: Annotated[int, Field(ge=13, le=150)]
    bio: str = ""
    isActive: bool = True

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscore allowed)")
        return v.lower()

    @field_validator("website", mode="before")
    @classmethod
    def validate_url(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

    @computed_field
    @property
    def display_name(self) -> str:
        if self.firstName and self.lastName:
            return f"{self.firstName} {self.lastName}"
        return self.username

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.followerCount >= 10000


class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likesCount: int = 0


class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: User
    comments: list[Comment] = Field(default_factory=list)
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]
    viewCount: int = 0
    isPublished: bool = False
    tags: list[str] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    status: Literal["draft", "published", "archieved"] = "draft"


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Password do not match")
        return self


### BlogPost Dictionary
post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "piyush",
        "email": "piyusht@gmail.com",
        "age": 19,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}


def pydantic_function():
    try:
        # User
        user = User(
            username="johndoe",
            email="john.doe@pydantic.com",
            password="hiudsh9y7qwt782wy7",
            age=20,
            firstName="John",
            lastName="Doe",
            website="piyushcodes.vercel.app",
        )
        print(user.model_dump_json(indent=4, by_alias=True, exclude={"password"}))

        # BlogPost
        p1 = BlogPost(**post_data)
        print(p1.model_dump_json(indent=4))
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    pydantic_function()
