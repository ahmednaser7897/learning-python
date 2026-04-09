#-------------
#Tuble
#-------------

#Tuble items are enclosed in ()
#you can remove () in definition
#Tuble are ordered to use index
#Tuble is immutable => you can not add or remove items
#tuble items is not unique
#you can add different data types in tuble

tuble1 = ("one","two","three","four",5,6,7)
tuble2="one","two","three","four",5,6,7
print(type(tuble1))#<class 'tuple'>
print(tuble1)#('one', 'two', 'three', 'four', 5, 6, 7)
print(type(tuble2))#<class 'tuple'>
print(tuble2)#('one', 'two', 'three', 'four', 5, 6, 7)
print(tuble1[0])#one
print(tuble1[-1])#7
print(tuble1[0:3])#('one', 'two', 'three')
print(tuble1[2:])#('three', 'four', 5, 6, 7)
print(tuble1[:2])#('one', 'two')
#tuble[start:end:step]
print(tuble1[:])#('one', 'two', 'three', 'four', 5, 6, 7)
#pick on and ignore one
print(tuble1[::2])#('one', 'three', 5, 7)
#show it reversed
print(tuble1[::-1])#(7, 6, 5, 'four', 'three', 'two', 'one')
#pick on and ignore one from the end
print(tuble1[::-2])#(7, 5, 'three', 'one')



#Assigning a value to a tuble
#its immutable 
tuble1 = ("one","two","three","four",5,6,7)
print(tuble1)#('one', 'two', 'three', 'four', 5, 6, 7)
#tuble1[0] = "ahmed"#TypeError: 'tuple' object does not support item assignment


#Tuble with one item
tuble1 = ("one",)
tuble2 = "one",
tuble3 = "one"#this is not tuble
tuble4 = ("one")#this is not tuble
print(type(tuble1))#<class 'tuple'>
print(tuble1)#('one',)
print(type(tuble2))#<class 'tuple'>
print(tuble2)#('one',)
print(type(tuble3))#<class 'str'>
print(tuble3)#one
print(type(tuble4))#<class 'str'>
print(tuble4)#one


#Tuble concatenation
tuble1 = ("one","two","three","four",5,6,7)
tuble2 = ("ahmed","nasr","mohamed")
print(tuble1+tuble2)#('one', 'two', 'three', 'four', 5, 6, 7, 'ahmed', 'nasr', 'mohamed')

#Tuble ,list,string repite
myString = "ahmed"
myList = ["ahmed","nasr","mohamed"]
myTuble = ("ahmed","nasr","mohamed")
print(myString*3)#ahmedahmedahmed
print(myList*3)#['ahmed', 'nasr', 'mohamed', 'ahmed', 'nasr', 'mohamed', 'ahmed', 'nasr', 'mohamed']
print(myTuble*3)#('ahmed', 'nasr', 'mohamed', 'ahmed', 'nasr', 'mohamed', 'ahmed', 'nasr', 'mohamed')


#-------------
#Tuble Methods
#-------------

#len() is a function that returns the length (int) of iterable
tuble1 = ("one","two","three","four",5,6,7)
print(len(tuble1))#7

#count() is a function that returns the number of times an item appears in the tuble
tuble1 = ("one","two","three","four",5,6,7)
print(tuble1.count("one"))#1

#index
tuble1 = ("one","two","three","four",5,6,7)
print(tuble1.index("two"))#1


#del
tuble1 = ("one","two","three","four",5,6,7)
del tuble1
#print(tuble1)#NameError: name 'tuble1' is not defined

#Tuble destructuring
tuble1 = ("one","two","three")
a,b,c = tuble1
print(a)#one
print(b)#two
print(c)#three

tuble1 = ("one","two","three","four")
#this ignore the 3erd item
a,b,_,c = tuble1
print(a)#one
print(b)#two
print(c)#three

tuble1 = ("one","two","three","four")
#this make last item as a list
#it can be any item last or stert or any
a,b,*c = tuble1
print(a)#one
print(b)#two
print(c)#['three', 'four']


#to change tables values change it to list then change it to tuble
#add or remove or any change
tuble1 = ("one","two","three","four")
tuble1 = list(tuble1)
tuble1[0] = "ahmed"
tuble1 = tuple(tuble1)
print(tuble1)#('ahmed', 'two', 'three', 'four')

