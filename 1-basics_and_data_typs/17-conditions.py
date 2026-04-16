#-------------
#Conditions
#-------------
#normal way
name ="ahmed"
price=100
isStudent=True
#country=input("Enter your country:").strip().lower()
country="ksa"
if country == "egypt" or country == "ksa":
    if isStudent:
        print(f"Welcome {name} from {country} your discount is {price*0.5}")
    else:
        print(f"Welcome {name} from {country} your discount is {price*0.4}")
elif country == "kuwait":
    if isStudent:
        print(f"Welcome {name} from {country} your discount is {price*0.3}")
    else:
        print(f"Welcome {name} from {country} your discount is {price*0.2}")
else:
    print(f"Welcome {name} from {country} your discount is {price*0.1}")


#One-line if statement:
a = 5
b = 2
if a > b: print("a is greater than b")



#ternary way or short way
a = 2
b = 330
massage=""
if a > b: #IF condition
    massage="a is greater than b" # Value if True
else: 
     massage="b is greater than a" #Value if False
print(massage)
# Value if True | IF condition |else | Value if False
massage="a is greater than b" if a > b else "b is greater than a"
print(massage)

name ="ahmed"
price=100
country="ksa"
discount = 0.1 if country == "egypt" or country == "ksa" else 0.2 if country == "kuwait" else 0.3
print(f"Welcome {name} from {country} your discount is {price*discount}")


#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
age = 20

if age < 18:
  pass #  Add underage logic later
else:
  print("Access granted")