# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class Member:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def say_hello(self):
        return f"Hello {self.__name}, Your Age Is {self.__age}"
    def age_in_days(self):
        return self.__age * 365
member_one = Member("Osama", 40)
print(member_one.say_hello())#Hello Osama, Your Age Is 40
print(member_one.age_in_days())#14600
# we can use the @property decorator to make the method look like an attribute when we call it
print(member_one.say_hello)#<bound method Member.say_hello of <__main__.Member object at 0x00000240355F6450>>
    

class Member:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def say_hello(self):
        return f"Hello {self.__name}, Your Age Is {self.__age}"
    @property
    def age_in_days(self):
        return self.__age * 365
   
member_one = Member("Osama", 40)
print(member_one.say_hello)#Hello Osama, Your Age Is 40
print(member_one.age_in_days)#14600
# we can also use the @property decorator to make the method look like an attribute when we call it
# so we can call it without parentheses and it will return the value of the method as an attribute
#print(member_one.age_in_days())#TypeError: 'int' object is not callable