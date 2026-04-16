#-------------
#Type Conversion
#-------------

#srt() method is used to convert to string
a=10
b=str(a)
print(type(b))#<class 'str'>
print(b)#10
print("*"*40)


#int() method is used to convert to integer
#float() method is used to convert to float
#complex() method is used to convert to complex
#[1] you cant converst from int to float and complex
#[2] you cant convert from float to int and complex
#[3] you cant not convert from complex to int or float

number=1
print(type(number))#<class 'int'>
print(float(number))#1.0
print(complex(number))#1+0j
number=1.0

print(type(number))#<class 'float'>
print(int(number))#1

print(complex(number))#1+0j

number=1+2j
print(type(number))#<class 'complex'>
#print(float(number))#TypeError: float() argument must be a string or a real number, not 'complex'
#print(int(number))##TypeError: float() argument must be a string or a real number, not 'complex'
print("*"*40)


#bool() method is used to convert to boolean
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
print("*"*40)


#tuple() method is used to convert to tuple
a="ahmed"
b=[1,2,3,4]
c={"a":1,"b":2,"c":3,"d":4}
d={1,2,3,4}
print(tuple(a))#('a', 'h', 'm', 'e', 'd')
print(tuple(b))#(1, 2, 3, 4)
#it will take keys
print(tuple(c))#('a', 'b', 'c', 'd')
print(tuple(d))#(1, 2, 3, 4)
print("*"*40)


#list() method is used to convert to list
a="ahmed"
b=(1,2,3,4)
c={"a":1,"b":2,"c":3,"d":4}
d={1,2,3,4}
print(list(a))#('a', 'h', 'm', 'e', 'd')
print(list(b))#(1, 2, 3, 4)
#it will take keys
print(list(c))#('a', 'b', 'c', 'd')
print(list(d))#(1, 2, 3, 4)
print("*"*40)



#set() method is used to convert to set
a="ahmed"
b=(1,2,3,4)
c={"a":1,"b":2,"c":3,"d":4}
d=[1,2,3,4]
print(set(a))#('a', 'h', 'm', 'e', 'd')
print(set(b))#(1, 2, 3, 4)
#it will take keys
print(set(c))#('a', 'b', 'c', 'd')
print(set(d))#(1, 2, 3, 4)
print("*"*40)



#dict() method is used to convert to dictionary
a="ahmed"
b=(1,2,3,4)
c=(("a",1),("b",2),("c",3))
e=[1,2,3,4]
d=[["a",1],["b",2],["c",3]]
f={1,2,3,4}
#String can not convert to dictionary
#print(dict(a))#this will raise an error

#print(dict(b))#this shap of tuple will raise an error
#but this shap of tuple that has items in shap of tuple with key and value works
print(dict(c))#{'a': 1, 'b': 2, 'c': 3}

#print(dict(e))##this shap of list will raise an error
#but this shap of list that has items in shap of list with key and value works
print(dict(d))#{'a': 1, 'b': 2, 'c': 3}


#Set can not convert to dictionary
#print(dict(f))#this will raise an error
print("*"*40)
