# empty function
def fun1(): ...


# basic functions
def say_hello(name: str) -> None:
    print(f"Hello, {name}")


def section(title: str) -> None:
    """Print a clearly visible section header to make the log easy to skim."""
    print(f"\n{'=' * 80}")
    print(f"{title}")
    print(f"{'=' * 80}")


# if the file is run directly (not imported as a module) then the main function is executed
if __name__ == "__main__":
    section(f"main from {__file__.split('/')[-1]}")
    say_hello("John")
    fun1()
