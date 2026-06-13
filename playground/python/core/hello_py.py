
## Looping
names: list[str] = [
    "hady",
    "ahmed",
    "mohamed",
    "ali",
    "ibrahimovic",
    "messi",
    "ronaldo",
    "neymar",
]

### loop approach 1
longest_name1 = []
for name in names:
    if len(name) > 7:
        longest_name1.append(name)
print(longest_name1)

### loop approach 2
longest_name2 = [name for name in names if len(name) > 7]
print(longest_name2)

# basic functions
def say_hello(name: str) -> str:
    print(f"Hello, {name}")


# empty function
def fun1(): ...


# class
class human:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name}"


# if the file is run directly (not imported as a module) then the main function is executed
if __name__ == "__main__":
    print("=================== main function =====================")
    say_hello("John")
    fun1()
    print(human("John"))
