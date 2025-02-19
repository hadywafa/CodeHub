from pydantic import BaseModel, PositiveInt
from datetime import datetime


# =================================================================================================================
def func(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


# =================================================================================================================


def main():
    user = User()
    user.name = 12
    


if __name__ == "__main__":
    main()
