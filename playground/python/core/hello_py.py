from hello_functions import section


section(f"{__file__.split('/')[-1]}")

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
longest_name1: list[str] = []
for name in names:
    if len(name) > 7:
        longest_name1.append(name)
print(longest_name1)

### loop approach 2
longest_name2 = [name for name in names if len(name) > 7]
print(longest_name2)
