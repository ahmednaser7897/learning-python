#-------------
#List
#-------------

#List is a collection of items in a particular order
#List is indexed
#List is ordered
#List is Mutable you can add or remove items
#List is iterable
list = ["one","two","three","four",5,6,7]
print(list)
print(list[0])#one
print(list[-1])#7
print(list[0:3])#['one', 'two', 'three']
print(list[2:])#['three', 'four', 5, 6, 7]
print(list[:2])#['one', 'two']
#list[start:end:step]
print(list[:])#['one', 'two', 'three', 'four', 5, 6, 7]
#pick on and ignore one
print(list[::2])#['one', 'three', 5, 7]
#show it reversed
print(list[::-1])#[7, 6, 5, 'four', 'three', 'two', 'one']
#pick on and ignore one from the end
print(list[::-2])#[7, 5, 'three', 'one']

list = ["one","two","three","four",5,6,7]
print(list)#['one', 'two', 'three', 'four', 5, 6, 7]
list[0] = "ahmed"
list[-1] = "0"
print(list)#['ahmed', 'two', 'three', 'four', 5, 6, '0']
list[1:3] = ["nasr","mohamed"] 
print(list)#['ahmed', 'nasr', 'mohamed', 'four', 5, 6, '0']
list[0:3] = [] 
print(list)#['four', 5, 6, '0']
list = ["one","two","three","four",5,6,7]
list[0:3] = ["new"] 
print(list)#[new, 'four', 5, 6, 7]

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)#[1, 2, 3, 4, 5, 6]




