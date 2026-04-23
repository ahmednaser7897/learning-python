# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food:
    def __init__(self, color):
        self.color = color
        print(f"Base Food Class Constructor with color {self.color}")
    def eat(self):
        return "Eating Food from Base Class"

# Inheritance: Is The Ability To Create A New Class From An Existing Class 
# And It Is One Of The Most Important Concepts In Object Oriented Programming
# The New Class Is Called Derived Class And The Existing Class 
# Is Called Base Class And The Derived Class Inherit All The Attributes And Methods From The Base Class 
# And It Can Add New Attributes And Methods Or Override The Existing Ones
# To Inherit From A Class We Need To Put The Name Of The Base Class In Parentheses After The Name Of The Derived Class
#once We Inherit From A Class We Can Create An Instance From The Derived Class 
# And It Will Have All The Attributes And Methods From The Base Class
class Apple(Food):
    def __init__(self, color, size):
        super().__init__(color)#this =  Food.__init__(self, color)
        self.size = size
        print(f"Derived Apple Class Constructor with color {self.color} and size {self.size}")
    def clean(self):
        return "Cleaning Apple from Derived Class"

food_one = Food("Yellow")#Base Food Class Constructor with color Yellow
# if we create an instance from the derived class it will call 
# the constructor of the base class first then the constructor of the derived class
apple_one = Apple("Red", "Large")#Base Food Class Constructor with color Red, Derived Apple Class Constructor with color Red and size Large

print(food_one.color)#Yellow
print(apple_one.color)#Red
print(apple_one.size)#Large
#print(food_one.size)#AttributeError: 'Food' object has no attribute 'size'
print(food_one.eat())#Eating Food from Base Class
print(apple_one.eat())#Eating Food from Base Class
#print(food_one.clean())#AttributeError: 'Food' object has no attribute 'clean'
print(apple_one.clean())#Cleaning Apple from Derived Class

       