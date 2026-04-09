#-------------
#Sets
#-------------
# [1] Set items are enclosed in {}
# [2] Set is not ordered and not indexed
# [3] Set indexing and slicing is not supported 
# [4] Set has only immutable items (numbers, strings, tuples)
# [5] List and dict are mutable so can not be added
# [6] Set is mutable => you can add or remove items
# [7] Set items is unique
# [8] Set is Mutable you can add or remove items

set1 = {"one","two",3,4}
print(type(set1))#<class 'set'>
print(len(set1))#4
#not orderd so each time it will be different
print(set1)#{3, 'two', 4, 'one'} , {3, 4, 'two', 'one'}

#not indexed
#print(set1[0])#KeyError: 0

#not slicing
#print(set1[0:2])#TypeError: 'set' object is not subscriptable

#has only immutable items
#like numbers, strings, tuples but not list and dict
#set1 = {"one","two",3,4,[1,2,3]}#TypeError: unhashable type: 'list'
set1 = {"one","two",3,4,(1,2,3)}
print(set1)#{'two', 3, 4, 'one', (1, 2, 3)}

#set has only unique items
#will not show error but will only show one
set1 = {"one","two",3,4,"one"}
print(set1)#{3, 4, 'two', 'one'}

