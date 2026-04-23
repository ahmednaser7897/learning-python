# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class Food:
    def __init__(self, color):
        self.color = color
        print(f"Base Food Class Constructor with color {self.color}")
    def eat(self):
        return "Eating Food from Base Class"


class Apple(Food):
    def __init__(self, color, size):
        super().__init__(color)#this =  Food.__init__(self, color)
        self.size = size
        print(f"Derived Apple Class Constructor with color {self.color} and size {self.size}")
    # we can override the eat method in the derived class to provide a different implementation for it
    def eat(self):
        return "Eating Apple from Derived Class"
    def clean(self):
        return "Cleaning Apple from Derived Class"

food_one = Food("Yellow")#Base Food Class Constructor with color Yellow
apple_one = Apple("Red", "Large")#Base Food Class Constructor with color Red, Derived Apple Class Constructor with color Red and size Large


print(food_one.eat())#Eating Food from Base Class
print(apple_one.eat())#Eating Apple from Derived Class
print("-----------------------------")

class BaseOne:
    def __init__(self):
        print("Base One Class Constructor")
    def method_one(self):
        return "Method One From Base One Class"
class BaseTwo:
    def __init__(self):
        print("Base Two Class Constructor")
    def method_two(self):
        return "Method Two From Base Two Class"
# Multiple Inheritance: Is The Ability To Create A New Class From More Than One Existing Class
# And It Is One Of The Most Important Concepts In Object Oriented Programming
class DerivedOne(BaseOne, BaseTwo):
    def data(self):
        return "Data From Derived One Class"

print(DerivedOne.mro())#[<class '__main__.DerivedOne'>, <class '__main__.BaseOne'>, <class '__main__.BaseTwo'>, <class 'object'>]
# when we create an instance from the derived class it will call the constructor 
# of the first base class then the constructor of the second base class
derived_one = DerivedOne()#Base One Class Constructor, Base Two Class Constructor

print(derived_one.method_one())#Method One From Base One Class
print(derived_one.method_two())#Method Two From Base Two Class

class DerivedTwo(DerivedOne):
    pass

derived_two = DerivedTwo()#Base One Class Constructor, Base Two Class Constructor
print(derived_two.method_one())#Method One From Base One Class
print(derived_two.method_two())#Method Two From Base Two Class
print(derived_two.data())#Data From Derived One Class
