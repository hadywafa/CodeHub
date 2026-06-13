# basic functions
def say_hello(name: str) -> None:
    print(f"Hello, {name}")


# empty function
def fun1(): ...


# if the file is run directly (not imported as a module) then the main function is executed
if __name__ == "__main__":
    print(f"============= main from {__file__.split('/')[-1]} =============")
    say_hello("John")
    fun1()
