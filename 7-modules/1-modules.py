# -----------------------------------
# --- Modules->Built In Modules  ----
# -----------------------------------
# [1] Modules are files that contain a set of functions and variables that can be used in other Python programs
# [2] Modules are used to organize code and to reuse code in different programs
# [3] Modules are imported using the import statement
# [4] you can import multiple modules in one line using comma
# -----------------------------------------------------------------------------------

# import random module
import random
print(random) #<module 'random' from 'C:\\Users\\ahmednaser\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>
print(random.randint(1, 10))  # prints a random integer between 1 and 10
print(dir(random)) # prints all the functions and variables in the random module
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'betavariate', 'choice', 'choices', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'shuffle', 'uniform']

#import one or more functions from a module
from random import randint, choice
print(randint(1, 10))  # prints a random integer between 1 and 10
print(choice(['apple', 'banana', 'cherry']))  # prints a random choice from the list

# import all functions from a module
from random import *
print(randint(1, 10))  # prints a random integer between 1 and 10

#import a module and give it an alias
import random as rnd
print(rnd.randint(1, 10))  # prints a random integer between 1 and 10

#import a function from a module and give it an alias
from random import randint as rint
print(rint(1, 10))  # prints a random integer between 1 and 10

# import many modules in one line
import math, datetime
print(math.sqrt(16))  # prints the square root of 16
print(datetime.datetime.now())  # prints the current date and time


# import a custom module
import my_module
print(my_module.say_hello("Bob"))  # prints "Hello, Bob!"
# import a custom module with alias
import my_module as mm
print(mm.add_numbers(5, 3))  # prints 8
print(mm.multiply_numbers(2, 4))  # prints 8