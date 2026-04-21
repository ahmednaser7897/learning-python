# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------
my_string = "Hello"
print(my_string.__class__)#<class 'str'>
print(dir(my_string))
print(my_string.upper())#HELLO
print(str.upper(my_string))#HELLO
print("-"*30)

class Mmember:
   def __init__(self,name):
      self.name = name
    
class Skill:
   def __init__(self):
      self.skills=["Python", "JavaScript", ]
    #this is a magic method which is called when we try to print the object and it gives us 
    # a human-readable output of the object instead of the default output 
    # which is the memory address of the object
    #the same like toString() method in Java and __repr__ method in Python but __str__ is more user-friendly and __repr__ is more developer-friendly
    #we can define the __str__ method in any class to give a human-readable output
   def __str__(self):
        return f"My Skills Are: {', '.join(self.skills)}"
    # this is a magic method which is called when we try to get the 
    # length of the object using the built-in len() function
    # so it enable us to use the len() function on the object and 
    # it will return the length of the container which is the skills list in this case
    # if we didn't define the __len__ method in the class and we 
    # try to use the len() function on the object it will raise a TypeError 
    # because the object is not a container and it doesn't have a length
   def __len__(self):
        return len(self.skills)
member_one = Mmember("Osama")
#this will print the default output which is the memory address of the object
#this is because we didn't define the __str__ method in the Mmember class
print(member_one)#<__main__.Mmember object at 0x000001EC07
myskill = Skill()
#this will print the output of the __str__ method which is a 
# human-readable output of the object
print(myskill)#My Skills Are: Python, JavaScript
print(myskill.__class__)#<class '__main__.Skill'>

#this will show us the error because we didn't define the __len__ method
#  in the Skill class and we are trying to use the len() function on the object 
# which is not a container and it doesn't have a length
#print(len(myskill))#TypeError: object of type 'Skill' has no len()

#this will print the output of the __len__ method which is the length of the skills list
print(len(myskill))#2
print(myskill.__len__())#2
print(len(myskill.skills))#['Python', 'JavaScript']




