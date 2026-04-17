# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group())#https://www.elzero.org:8080/category.php?article=105?name=how-to-do
print(search.groups())#('https', 'www', 'elzero', 'org', '8080', 'category.php?article=105?name=how-to-do')

for group in search.groups():
  print(group, end=" ")#https, www, elzero, org, 8080, category.php?article=105?name=how-to-do
print()
print(f"Protocol: {search.group(1)}")#Protocol: https
print(f"Sub Domain: {search.group(2)}")#Sub Domain: www
print(f"Domain Name: {search.group(3)}")#Domain Name: elzero
print(f"Top Level Domain: {search.group(4)}")#Top Level Domain: org
print(f"Port: {search.group(5)}")#Port: 8080
print(f"Query String: {search.group(6)}")#Query String: category.php?article=105?name=how-to-do