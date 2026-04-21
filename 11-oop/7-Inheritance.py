# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food:
    def __init__(self, color):
        self.color = color
        print(f"Base Food Class Constructor with color {self.color}")
    def eat(self):
        return "Eating Food from Base Class"

class Apple(Food):
    def __init__(self, color):
        super().__init__(color)#this =  Food.__init__(self, color)
        print(f"Derived Apple Class Constructor with color {self.color}")

food_one = Food("Yellow")#Base Food Class Constructor with color Yellow
apple_one = Apple("Red")#Base Food Class Constructor with color Red, Derived Apple Class Constructor with color Red

print(food_one.color)#Yellow
print(apple_one.color)#Red
       