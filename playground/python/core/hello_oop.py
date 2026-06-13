# class
class human:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name}"

    def say_hello(self) -> str:
        return f"Hello, {self.name}"

    def say_goodbye(self) -> str:
        return f"Goodbye, {self.name}"

    def change_name(self, new_name: str) -> None:
        self.name = new_name


# if the file is run directly (not imported as a module) then the main function is executed
if __name__ == "__main__":
    print(f"============= main from {__file__.split('/')[-1]} =============")
    human1 = human("John Doe")
    print(human1)
    print(human1.say_hello())
    human1.change_name("Jane Doe")
    print(human1)
