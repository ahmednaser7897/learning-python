# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

# we can access the attributes from outside the class which is not good for data protection
print("-"*10+"Example with Public Attributes(no encapsulation)"+ "-"*10)
class Member:
    def __init__(self, name, age):
        self.name = name#public attribute
        self.age = age#public attribute
member_one = Member("Osama", 40)
print(member_one.name)#Osama
print(member_one.age)#40



print("-"*10+"Example with Protected Attributes(no encapsulation)"+ "-"*10)
#when we use protected attributes we can access them from outside the class 
# but it is not recommended to do that because it is not good for data protection
class Member:
    def __init__(self, name, age):
        self._name = name#protected attribute
        self._age = age#protected attribute
member_one = Member("Osama", 40)
print(member_one._name)#Osama
print(member_one._age)#40



print("-"*10+"Example with Private Attributes(encapsulation)"+ "-"*10)
class Member:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
member_one = Member("Osama", 40)
# we cannot access the private attributes from outside the class which is good for data protection
# print(member_one.__name)  # This would raise an AttributeError
# print(member_one.__age)   # This would raise an AttributeError
print(member_one.get_name())  # Osama
print(member_one.get_age())   # 40
member_one.set_name("Ahmed")
member_one.set_age(30)
#in some cases we can access the private attributes from outside the class by using name mangling
# but it is not recommended to do that because it is not good for data protection
print(member_one._Member__name)  # Ahmed
print(member_one._Member__age)   # 30