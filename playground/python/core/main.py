from hello_functions import say_hello, section


# if the file is run directly (not imported as a module) then the main function is executed
if __name__ == "__main__":
    section(f"main from {__file__.split('/')[-1]}")
    say_hello("Hady")
