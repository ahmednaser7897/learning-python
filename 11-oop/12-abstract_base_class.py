# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------



print("-"*10+"Example with no abstract methods and class"+ "-"*10)
class ProgrammingLanguage():
    def has_oop(self):
        return "Yes"
class Python(ProgrammingLanguage):
    def has_oop(self):
        return "Yes"
class Pascal(ProgrammingLanguage):
    def has_oop(self):
        return "No"
programmingLanguage=ProgrammingLanguage()
python = Python()
pascal = Pascal()
# we can use the same method name in different classes and it will work correctly because of polymorphism
# but its not logical to have a method that returns "Yes" in the base class 
# and then override it in the derived class to return "No" because it is not good 
# for data protection and it is not good for code readability
# so programmingLanguage should be an abstract class and the has_oop method 
# should be an abstract method that must be implemented in the derived classes
print(programmingLanguage.has_oop())#Yes
print(python.has_oop())#Yes
print(pascal.has_oop())#No

print("-"*10+"Example with abstract methods and class"+ "-"*10)

from abc import ABCMeta, abstractmethod
# we cannot create an object from an abstract class because it is not complete and it is not logical to do that
class ProgrammingLanguage(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
class Python(ProgrammingLanguage):
    def has_oop(self):
        return "Yes"
class Pascal(ProgrammingLanguage):
    def has_oop(self):
        return "No"
# we cannot create an object from the abstract class because it is not complete and it is not logical to do that
# programmingLanguage=ProgrammingLanguage()#TypeError: Can't instantiate abstract class ProgrammingLanguage with abstract method has_oop
python = Python()
pascal = Pascal()
print(python.has_oop())#Yes
print(pascal.has_oop())#No
