#-------------
#Membership Operators
#-------------

#[1] in
#[2] not in

#Syntax
#[1] name in iterable
#[2] name not in iterable

#string
name = "ahmed"
print("a" in name) #True
print("a" not in name) #False

#list
list = ["ahmed","nasr","mohamed"]
print("ahmed" in list) #True
print("ahmed" not in list) #False

countrysList1=["egypt","libya","ksa"]
discount1=10
countrysList2=["usa","canada","italy"]
discount2=20
country="usa"

if country in countrysList1:
    print(f"Welcome {name} from {country} your discount is {discount1}")
elif country in countrysList2:
    print(f"Welcome {name} from {country} your discount is {discount2}")
else:
    print(f"Welcome {name} from {country} your discount is 0")

discount=10 if country in countrysList1 else 20 if country in countrysList2 else 0
print(f"Welcome {name} from {country} your discount is {discount}")