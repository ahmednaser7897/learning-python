# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
#decorator is a higher-order function that takes another function func as an argument
#  and defines an inner function wrapper that adds some functionality 
# before and after calling the original function func. The wrapper function is then returned,
#  effectively replacing the original function with the enhanced version.

def decorator(func):
    def wrapper():#any name its just for the inner function that will wrap the original function func.
        print("Before the function call")
        func() #call the original function func inside the wrapper to execute its functionality.
        print("After the function call")
    return wrapper #return the wrapper function that will replace the original function when the decorator is applied.


#this is a way to apply the decorator to a function without using the @ syntax.
#but this is not recommended way
print("-"*10+"Old Way Decorator"+ "-"*10)
def say_hello():
    print("Hello, World!")  
# Apply the decorator to the say_hello function
decorated_function = decorator(say_hello)
# Call the decorated function
decorated_function()


print("-"*10+"New Way Decorator"+ "-"*10)
# Apply the decorator to the say_goodbye function using the @ syntax
@decorator
def say_goodbye():
    print("Goodbye, World!")
# Call the decorated function
say_goodbye()



# ---------------------------------------------
# -- Decorators => Decorator with Parameters --
# ---------------------------------------------
print("-"*10+"Decorator with Parameters"+ "-"*10)


def add_numbers(a,b):
    return a + b
#add_numbers(5, 3) #error TypeError: wrapper() takes 0 positional arguments but 2 were given
#The error occurs because the wrapper function defined inside the decorator does not accept any parameters,
#  but the add_numbers function expects two parameters.

# To fix this, we need to modify the wrapper function to accept the same parameters as the original function.
def decorator(func):
    def wrapper(*args, ): #accept any number of positional and keyword arguments
        print("Before the function call")
        result = func(*args,) #call the original function with the passed arguments and store the result
        print("After the function call")
        return result #return the result of the original function
    return wrapper
 #Apply the decorator to the my function using the @ syntax
@decorator
def add_numbers(*args):
    return sum(args)

# Call the decorated function
print(add_numbers(5, 3,2)) #Before the function call, After the function call, 10

# -----------------------------------------------
# -- Decorators => Decorator SppedTest Example --
# -----------------------------------------------
print("-"*10+"Decorator SppedTest Example"+ "-"*10)

from time import time
def speedTest(fun):
    def wrapper():       
       start=time()
       result=fun()
       end=time()
       print(f"the function {fun.__name__} took {end-start} seconds to execute")
       return result
    return wrapper

@speedTest
def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

print(my_function()) #the function my_function took 0.1 seconds to execute, 499999500000