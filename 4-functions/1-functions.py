#-------------
#Python functions
#-------------
#[1] A function is a block of code which only runs when it is called.
#[2] A function run when it is called.
#[3] You can pass data, known as parameters, into a function. A function can return data as a result.
#[4] A function can return data as a result or it can return nothing (return None).
#[5] A function create to  prevent DRY code (Don't Repeat Yourself) and to make the code more organized and readable.

#-------------
#Basic function
#-------------
#Creating a function it can return nothing or return a value
def my_function1():
    print("Hello from a function1")
my_function1()#Hello from a function1

#it can return a value and we can store it in a variable
def my_function2():
    return "Hello from a function2"
print(my_function2())#Hello from a function2
my_result = my_function2()
print(my_result)#Hello from a function2

#-------------
#function with parameters
#-------------
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument

#function with parameters
name="Mohamed"
def my_function3(name):
    return f"Hello {name} from a function3"
print(my_function3("Ahmed"))#Hello Ahmed from a function3
print(my_function3(name))#Hello Mohamed from a function3
#You can send arguments with the key = value syntax.
print(my_function3(name="Mohamed"))#Hello Mohamed from a function3

#Combining Positional-Only and Keyword-Only
#You can combine both argument types in the same function.

#Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)#50
print("-"*50)
def add_numbers(num1,num2):
    if type(num1) != int or type(num2) != int:
        return "Error: Both parameters must be integers."
    return num1+num2
print(add_numbers(1,2))#3
print(add_numbers("1",2))#Error: Both parameters must be integers.


#function with default parameters
#default parameters amust be at the end of the parameters list
#def my_function4(name="Ahmed",age):#SyntaxError: non-default argument follows default argument
def my_function4(name="Ahmed",age=20):
    return f"Hello {name}, you are {age} years old."
print(my_function4())#Hello Ahmed, you are 20 years old.
print(my_function4("Mohamed"))#Hello Mohamed, you are 20 years old.
print(my_function4("Mohamed", 25))#Hello Mohamed, you are 25 years old.

#---------------------------------------------------------
#function packing and unpacking arguments *args
#---------------------------------------------------------
#this is a short hand for a function that takes any number of arguments and returns them as a tuple
#it is for normal iterable like list, tuple, set but not for dict
#*args type is tuple
#normal parameters
def say_hello(name1,name2,name3):
    pepols = [name1,name2,name3]
    for name in pepols:
        print(f"Hello {name}")
say_hello("Ahmed","Mohamed","Ali")#Hello Ahmed\nHello Mohamed\nHello Ali
#say_hello("Ahmed","Mohamed","Ali","Sayed")#TypeError: say_hello() takes 3 positional arguments but 4 were given

#Packing *args
def say_hello2(*peoples):
    for name in peoples:
        print(f"Hello {name}")
say_hello2("Ahmed","Mohamed","Ali")#Hello Ahmed\nHello Mohamed\nHello Ali
say_hello2("Ahmed","Mohamed")#Hello Ahmed\nHello Mohamed
def show_info(name ,*skills):
     print(f"Hello {name}, your skills are: " + ", ".join(f"- {skill}" for skill in skills))

#can send any number of arguments but must be in the form of normal parameters
show_info("Ahmed","Python","JavaScript")#Hello Ahmed, your skills are: - Python, - JavaScript

#can send a list but must unpack it using *
list_of_skills = ["Python","JavaScript"]
show_info("Mohamed",*list_of_skills)#Hello Mohamed, your skills are: - Python, - JavaScript



#---------------------------------------------------------
#function packing and unpacking arguments **kwargs
#---------------------------------------------------------
#this is a short hand for a function that takes any number of keyword arguments 
#and returns them as a dictionary
#it is not for normal iterable like list, tuple, set 
#**kwargs type is dict
#normal parameters
# def say_hello3(**peoples):
#     for name in peoples:
#         print(f"Hello {name}")
# say_hello3("Ahmed","Mohamed","Ali")#TypeError: say_hello3() takes 0 positional arguments but 3 were given
#Packing **kwargs


def show_info2(name,**skills):
    print(f"Hello {name}, your skills are: " + ", ".join(f"- {skill}: {level}" for skill, level in skills.items()))
#can send any number of keyword arguments but must be in the form of key=value
show_info2("Ahmed",Python="Advanced",JavaScript="Intermediate")#Hello Ahmed, your skills are: - Python: Advanced, - JavaScript: Intermediate

#can send a dictionary but must unpack it using **
skills = {"Python":"Advanced","JavaScript":"Intermediate"}
show_info2("Mohamed",**skills)#Hello Mohamed, your skills are: - Python: Advanced, - JavaScript: Intermediate
print("-"*100)
#---------------------------------------------------------
#function packing and unpacking Example
#---------------------------------------------------------

skils=("dart","flutter","c++")
skilsWithLevel={
    "python":"Advanced",
    "javascript":"Intermediate",
    "dart":"Beginner",}
def show_info3(name,*skills,**skillsWithLevel):
    print(f"Hello {name}")
    if  len(skills)==0 :
        print("You have no normal skills.")
    else:
        print("Your normal skills are:")
        for skill in skills:
            print(f"  - {skill}")
    if  len(skillsWithLevel)==0 :
        print("You have no skills with levels.")
    else:
        print("Your skills with levels are:")
        for skill, level in skillsWithLevel.items():
            print(f"  - {skill}: {level}")
    print("-"*30)

#we can  not sending  *args and **kwargs 
#because they are optional and can be empty 
# we must send the normal parameters
show_info3("Ahmed",*skils,**skilsWithLevel)
show_info3("Mohamed")
show_info3("khalid",*skils)
show_info3("naser",**skilsWithLevel)

