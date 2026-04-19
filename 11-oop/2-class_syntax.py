
# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function

class Member :
    def __init__(self):
        print("new member created")

Member()#new member created
Member()#new member created
Member()#new member created
print(dir(Member))#['__doc__', '__init__', '__module__', '__dict__', '__weakref__', '__str__', '__repr__', '__eq__', '__ne__', '__hash__', '__bool__', '__getattribute__', '__setattr__', '__delattr__', '__dir__', '__format__', '__sizeof__', '__subclasshook__']

member1 = Member()#new member created
member2 = Member()#new member created

#we can get what is the class of the object by using __class__ attribute
print(member1.__class__)#<class '__main__.Member'>