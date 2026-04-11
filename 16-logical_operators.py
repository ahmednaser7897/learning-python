#-------------
#Logical Operators
#-------------

#[1] and
#[2] or
#[3] not

a = True
b = False

print(a and b) #False
print(a or b) #True
print(not a) #False

#any empty data is false
print(bool("")) #False
print(bool(0)) #False
print(bool(None)) #False
print(bool(False)) #False
print(bool([])) #False
print(bool({})) #False
print(bool(())) #False
print(bool(set())) #False

print("*"*40)
#all data is true
print(bool("a")) #True
print(bool(1)) #True
print(bool([1,2,3])) #True
print(bool({"a":1,"b":2})) #True
print(bool((1,2,3))) #True
