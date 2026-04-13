#-------------
#Python Scope
#-------------

# Python has a global scope
# Python has a local scope
# Python has a built-in scope

x=1# global scope
def printGlobalX():
    print(f"x={x} in global scope")
printGlobalX()#x=1 in global scope
def my_function():
    y=2# local scope
    print(f"x={x}, y={y} in function1 scope")
#print(f"x={x}, y={y} in global scope")#error: name 'y' is not defined
my_function()#x=1, y=2 in function1 scope

def my_function2():
    x=10# local scope
    y=2# local scope
    print(f"x={x}, y={y} in function2 scope")
my_function2()#x=10, y=2 in function2 scope
printGlobalX()#x=1 in global scope

#if we want to change the value of a global variable inside a function 
# we can use the global keyword
def my_function3():
    #if x is not defined in global scope 
    # it will create a new variable x in global scope and assign it the value of 15
    #and all functions that use x will use the new value of x 
    # but it must be called before any function that uses x to see the change in value of x
    #if x is defined in global scope it will change the value of x in global scope to 15 and all functions that use x will use the new value of x
    global x
    x=15# this will change the value of x in global scope
    print(f"x={x} in function3 scope")
my_function3()#x=15 in function3 scope
printGlobalX()#x=15 in global scope
print("-"*50)

#Nonlocal Keyword
#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.
# you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1())#Jane
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())#hello
print("-"*50)

#The LEGB Rule
#Python follows the LEGB rule when looking up variable names, and searches for them in this order:
#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
print("-"*50)


#-------------
#Python functions recursion
#-------------
#Recursion is a programming technique where a function calls itself in order to solve a problem.
#A recursive function is a function that calls itself in order to solve a problem.

#factorial of a number is the product of all positive integers less than or equal to that number.
#factorial of 5 is 5*4*3*2*1=120
#factorial of 0 is 1
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print("*"*50)
#CLEAAN STRING FROM DUPLICATE LETTERS RECURSIVE
def clean_string(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:#"WWWOOORRRLDD"
        print(f"Duplicate found: {word[0]}{word[1]} in {word}")
        return clean_string(word[1:])
    print(f"No duplicate found: {word[0]}{word[1]} in {word}")
    return word[0] + clean_string(word[1:])
print(clean_string("WWWOOORRRLDD"))#WORLD
print("*"*50)

#-------------
#Python functions =>Lambda functions
#anonymous function is a function that is defined without a name.
#Lambda functions are anonymous functions that can take any number of arguments but can only have one expression
#lambda functions are used for short and simple functions that are not reused elsewhere in the code.
#lambda type is function
#lambda function syntax: lambda arguments: expression
#its for one line function
#-------------


def say_hello(name):
    return f"Hello {name} from a normal function"
print(say_hello("Ahmed"))#Hello Ahmed from a normal function
say_hello_lambda = lambda name: f"Hello {name} from a lambda function"
print(say_hello_lambda("Ahmed"))#Hello Ahmed from a lambda function
print(say_hello.__name__)#say_hello
print(say_hello_lambda.__name__)#<lambda>
print("*"*50)


#-------------
#Python pass
#-------------
#pass is a null statement in Python. It is used as a placeholder for future code. It is used when a statement is required syntactically but you do not want any code to be executed.
def my_function4():
    pass
my_function4()