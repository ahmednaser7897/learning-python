#-------------
#Loops :For
#-------------
#For is a loop that executes a block of code for each item in an iterable
#Syntax
#for item in iterable:
    #do something
#else:
    #do something after loop end
names = ["ahmed","mohamed","ali"]
for name in names:
    print(f"#{str(names.index(name)+1).zfill(2)} {name}")
else:
    print("loop is end")

#Range
# is a function that returns a sequence of numbers
#Syntax
#range(start,stop,step)
for i in range(1,11):
    print(i)
else:
    print("*"*40)
#enumerate
# is a function that returns a sequence of tuples
#Syntax
#enumerate(iterable,start=0)
names = ["ahmed","mohamed","ali"]
for i,name in enumerate(names):
    print(f"#{str(i+1).zfill(2)} {name}")
else:
    print("*"*40)

#dict
# is a function that returns a dictionary
#Syntax
#dict(iterable)
myValus={
    "ahmed":10,
    "mohamed":20,
    "ali":30
}

for value in myValus:
    #value is the key
    #myValus[value] is the value
    print(f"#{str(myValus[value]).zfill(2)} {value}")
else:
    print("*"*40)

for key,value in myValus.items():
    print(f"#{str(value).zfill(2)} {key}")
  
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("hellow python")

print("*"*40)
