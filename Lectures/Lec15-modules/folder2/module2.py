from sys import path
path.append("folder1")

import module1



def say_hello2():
    # __name__ is set to modules name if imported
    # __name__ set to __main__ if ran directly as standalone script
    print(f"{__name__} says hello")



module1.say_hello1()