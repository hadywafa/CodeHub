from pydantic import BaseModel
from datetime import datetime


# =================================================================================================================
def func(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None


# =================================================================================================================


def main():
    user: User = User()
    user.name = 12


if __name__ == "__main__":
    main()
