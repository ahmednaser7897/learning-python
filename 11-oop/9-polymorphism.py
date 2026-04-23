# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

from pyclbr import Class


n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)
# Polymorphism: Is The Ability To Use The Same Operator Or Method With Different Types Of Data
# And It Is One Of The Most Important Concepts In Object Oriented Programming
# In Python We Can Use The Same Operator Or Method With Different Types Of Data And It Will Work Correctly
# For Example The + Operator Can Be Used To Add Two Numbers Or To Concatenate Two Strings
# The len() Function Can Be Used To Get The Length Of A String Or A List Or A Dictionary
print(len([1, 2, 3, 4, 5, 6]))#6
print(len((1, 2, 3, 4, 5)))#5
print(len("Osama Elzero"))#12
print(len({"Key_One": 1, "Key_Two": 2}))#2

# We Can Also Use Polymorphism With Classes And Objects By Overriding The Methods 
# In The Derived Class To Provide A Different Implementation For Them
# For Example We Can Create A Base Class With A Method And Then Create A Derived Class That Inherit From The Base Class
# And Override The Method To Provide A Different Implementation For It
class BaseClass:
    def method(self):
        return "Method From Base Class"
    
class DerivedClass(BaseClass):
    def method(self):
        return "Method From Derived Class"

base = BaseClass()
derived = DerivedClass()

print(base.method())#Method From Base Class
print(derived.method())#Method From Derived Class