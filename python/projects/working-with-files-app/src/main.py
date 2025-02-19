from datetime import datetime
from dataclasses import dataclass


# =================================================================================================================
def func(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class User:
    id: int
    name: str = "John Doe"


# =================================================================================================================


def main():
    user = User(id=1, name="John Doe")
    user
    print(user)


if __name__ == "__main__":
    main()
