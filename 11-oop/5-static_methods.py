# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Member:
   # This is a class attribute which is shared by all instances created from the class 
   # and it can be accessed by using the class name or the instance name
  not_allowed_names = ["Admin", "Root", "Sys"]
  users_count = 0
  def __init__(self, first_name, middle_name, last_name, gender):
    # Every Time We Create An Instance From The Class We Increment 
    # The Users Count By 1 To Keep Track Of The Number Of Members Created From The Class
    Member.users_count += 1
    print(f"New Member Created, Total Members: {Member.users_count}")
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  # This Is A Class Method Which Take Cls Parameter To Point To The Class Itself And It Is Marked 
  # With @classmethod Decorator To Flag It As Class Method
  # we call it from the class name not the instance name because it is a class method 
  # and it doesn't require creation of a class instance
  # we also can call it from the instance name but it is not recommended to avoid confusion and 
  # to make it clear that we are calling a class method not an instance method
  @classmethod
  def get_users_count(cls):
      return f"Total Members Created From The Class Is: {cls.users_count}"
  
  # This Is A Static Method Which Take No Parameters And It Is Marked With 
  # @staticmethod Decorator To Flag It As Static Method
  # we call it from the class name not the instance name because it is a static method
  # and it doesn't require creation of a class instance
  # we also can call it from the instance name but it is not recommended to avoid confusion and
  # to make it clear that we are calling a static method not an instance method
  @staticmethod
  def static_method_example():
      return "This Is A Static Method Example"

  def full_name(self):
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"
  def delete_member(self):
      Member.users_count -= 1
      print(f"Member Deleted, Total Members: {Member.users_count}")     

  def get_all_info(self):
    if self.fname in Member.not_allowed_names:
      return f"Sorry {self.fname}, You Are Not Allowed To Join"
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"
  
member_one = Member("Osama", "Mohamed", "Elsayed", "Male")#New Member Created, Total Members: 1

member_two = Member("Admin", "Ali", "Mahmoud", "Male")#New Member Created, Total Members: 2

# we call it from the class name not the instance name because it is a class method 
# and it doesn't require creation of a class instance
# we also can call it from the instance name but it is not recommended to avoid confusion and 
# to make it clear that we are calling a class method not an instance method
print(Member.get_users_count())#Total Members Created From The Class Is: 2
print(member_one.get_users_count())#Total Members Created From The Class Is: 2


# we call it from the class name not the instance name because it is a static method 
# and it doesn't require creation of a class instance
# we also can call it from the instance name but it is not recommended to avoid confusion and 
# to make it clear that we are calling a static method not an instance method
print(Member.static_method_example())#This Is A Static Method Example
print(member_one.static_method_example())#This Is A Static Method Example