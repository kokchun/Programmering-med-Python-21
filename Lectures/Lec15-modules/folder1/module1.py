def say_hello1():
    # __name__ is set to modules name if imported
    # __name__ set to __main__ if ran directly as standalone script
    print(f"{__name__} says hello")

# to run say_hello() as standalone and not imported use
if __name__ == "__main__":
    say_hello1()

