
#-------------
#Set Methods
#-------------

#add() is a method that adds an item to the set
set1 = {"one","two",3,4}
#set1.add(5,6)#TypeError: add() takes at most 1 positional arguments but 2 were given
set1.add(5)
print(set1)#{3, 4, 5, 'two', 'one'}

#clear() is a method that removes all items from the set
set1 = {"one","two",3,4}
set1.clear()
print(set1)#{} or set()

# union() is a method that returns a new set with all items from both sets
set1 = {"one","two",3,4}
set2 = {5,6,7,8}
set3 = set1.union(set2)
set4 = set1 | set2
print(set3)#{3, 4, 5, 6, 7, 8, 'two', 'one'}
print(set4)#{3, 4, 5, 6, 7, 8, 'two', 'one'}


#copy() is a method that returns a copy of the set
#this is shallow copy 
#this is not deep copy
#so when chane one it will not change the other
set1 = {"one","two",3,4}
set2 = set1.copy()
set1.add(5)
print(set1)#{3, 4, 5, 'one', 'two'}
print(set2)#{'two', 3, 4, 'one'}

#remove() is a method that removes an item from the set
set1 = {"one","two",3,4}
set1.remove(3)
#set1.remove(5)#KeyError: value must be in set 
print(set1)#{4, 'two', 'one'}


#discard() is a method that removes an item from the set
set1 = {"one","two",3,4}
set1.discard(5)#no error
set1.discard(3)
print(set1)#{4, 'two', 'one'}

#pop() is a method that removes and returns an random item from the set
set1 = {"one","two",3,4}
set1.pop()
print(set1)#{3, 4, 'two'}



#update() is a method that adds items from another set to the current set
set1 = {"one","two",3,4}
set2 = {3,4,5,6,7,8}
set1.update(set2)
print(set1)#{3, 4, 5, 6, 7, 8, 'two', 'one'}
set1.update([3,4,5,6,7,8])
print(set1)#{3, 4, 5, 6, 7, 8, 'two', 'one'}


# difference() is a method that returns a new set with items from the first set that are not in the second set
# dose not change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
set3 = set1.difference(set2)
#the same like
#set3 = set1 - set2
print(set3)#{'two', 3, 4, 'one'}

# difference_update() is a method that removes items from the first set that are also in the second set 
# change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
set1.difference_update(set2)
#the same like
# set1 -= set2
print(set1)#{'two', 3, 4, 'one'}

# intersection() is a method that returns a new set with common items from both sets
# dose not change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
set3 = set1.intersection(set2)
#set3 = set1 & set2
print(set3)#{5, 6}

# intersection_update() is a method that removes items from the first set that are not in the second set 
# change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
set1.intersection_update(set2)
#set1 &= set2
print(set1)#{5, 6}





#symmetric_difference() is a method that returns a new set with items from both sets that are not in both sets
# dose not change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
set3 = set1.symmetric_difference(set2)
#set3 = set1 ^ set2
print(set3)#{3, 4, 7, 8, 'one', 'two'}

# symmetric_difference_update() is a method that removes items from the first set that are not in the second set 
# change the original set
set1 = {"one","two",3,4,5,6}
set2 = {5,6,7,8}
#set1.symmetric_difference_update(set2)
set1 ^= set2
print(set1)#{3, 4, 7, 8, 'one', 'two'}

#issuperset() is a method that returns True if all items in the second set are present in the first set
set1 = {"one","two",3,4}
set2 = {3,4,}
set3={3,4,5,6}

print(set1.issuperset(set2))#True
print(set1.issuperset(set3))#False


#issubset() is a method that returns True if all items in the first set are present in the second set
set1 = {"one","two",3,4}
set2 = {3,4,}
set3={3,4,5,6}

print(set1.issubset(set2))#False
print(set2.issubset(set3))#True

#isdisjoint() is a method that returns True if two sets have no common items
set1 = {"one","two",3,4}
set2 = {3,4,}
set3={5,6,7,8}

print(set1.isdisjoint(set2))#False
print(set2.isdisjoint(set3))#True



thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) #this will raise an error because the set no longer exists

