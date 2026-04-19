# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# ----------------------------------------------------------

class Member :
    #this is the constructor of the class and it is called every time we create an instance from the class
    #it must take the self parameter which point to the instance created from the class and it must be the first parameter in the constructor
    def __init__(self, first_name, last_name):
        #we can create instance attributes by using self and assign it to the value of the parameter
        #it can only created inside the constructor and it can be different for each instance created from the class
        self.first_name = first_name
        self.last_name = last_name
        print(f"new member created with name: {self.first_name} {self.last_name}")
    #this is an instance method which take self parameter and it can access the instance attributes and return the full name of the member
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

member1 = Member("Ahmed", "Nasser")#new member created with name: Ahmed Nasser
#this get Instance Attributes
print(dir(member1))#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']

print(member1.first_name)#Ahmed
print(member1.last_name)#Nasser

member2 = Member("Mohamed", "Ali")#new member created with name: Mohamed Ali
print(member2.full_name())#Mohamed Ali
print("-"*30)

class Member:
  def __init__(self, first_name, middle_name, last_name, gender):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  def full_name(self):
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"

  def get_all_info(self):
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)#Osama Mohamed Elsayed
print(member_two.fname)#Ahmed
print(member_three.fname)#Mona

print(member_two.full_name())#Ahmed Ali Mahmoud
print(member_two.name_with_title())#Hello Mr Ahmed

print(member_one.get_all_info())#Hello Mr Osama, Your Full Name Is: Osama Mohamed Elsayed