# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search)#<re.Match object; span=(0, 2), match='OO'>
print(my_search.span())#(0, 2)
print(my_search.string)#OOsamaEElzero
print(my_search.group())#OO

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:
  print("This is A Valid Email")#This is A Valid Email
  print(is_email.span())#(0, 12)
  print(is_email.string)#os@osama.com
  print(is_email.group())#os@osama.com
else:
  print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

  empty_list.append(search)

  print("Email Added")

else:

  print("Invalid Email")

for email in empty_list:

  print(email)