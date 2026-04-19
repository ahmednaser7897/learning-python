# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
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
print(Member.not_allowed_names)#['Admin', 'Root', 'Sys']
print(Member.users_count)#2
# we can access class attributes by using the class name or the instance name 
# but it is recommended to use the class name to avoid confusion and to make it clear that we are accessing 
# a class attribute not an instance attribute
print(member_one.not_allowed_names)#['Admin', 'Root', 'Sys']
print(member_two.users_count)#2

print(member_one.get_all_info())#Hello Mr Osama, Your Full Name Is: Osama Mohamed Elsayed
print(member_two.get_all_info())#Sorry Admin, You Are Not Allowed To Join

member_one.delete_member()#Member Deleted, Total Members: 1
member_two.delete_member()#Member Deleted, Total Members: 0
print(Member.users_count)#0
