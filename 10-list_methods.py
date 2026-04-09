#-------------
#List Methods
#-------------
################
#List is Mutable you can add or remove items
    #1-Item Assignment: You can change an individual element directly using 
    # its index (e.g., my_list[0] = 10).
    #2-Dynamic Sizing: You can add elements (using .append(), .extend(), or .insert())
    #and remove them (using .remove(), .pop(), or del).
    #3-Same Identity: When you modify a list, it remains the same object in memory.
    #You can verify this by checking that its id() 
    #remains constant before and after the change.
    #4-Contrast with Tuples: Unlike lists, tuples are immutable; once created, their elements cannot be changed or reassigned.
    #5-Slice Assignment: You can replace a slice of the list with another iterable (e.g., my_list[1:3] = ["a", "b"]).
    #6-Add/Remove Methods: Functions like append(), insert(), remove(), pop(), and del allow you to modify the list's contents.
    #7-In-Place Operations: Many list methods (like sort() or reverse()) modify the list directly (in-place) rather than returning a new one.
################


#len() is a function that returns the length (int) of iterable
list = ["ahmed","nasr","mohamed"]
print(len(list))#3

#append() is a function that adds an item to the end of the list
list = ["ahmed","nasr","mohamed"]
list.append("sayed")
list.append([1,2,3])
print(list)#['ahmed', 'nasr', 'mohamed', 'sayed', [1, 2, 3]]
print(list[4])#[1,2,3]
print(list[4][1])#2

#extend() is a function that adds the elements of a list to the end of the current list
list = ["ahmed","nasr","mohamed"]
list.extend([1,2,3])
print(list)#['ahmed', 'nasr', 'mohamed', 1, 2, 3]



#insert() is a function that adds an item to the list at the specified index
list = ["ahmed","nasr","mohamed"]
list.insert(0,"khaled")
print(list)#['khaled', 'ahmed', 'nasr', 'mohamed']

#remove() is a function that removes an item from the list
list = ["ahmed","nasr","mohamed"]
list.remove("nasr")
print(list)#['ahmed', 'mohamed']

#sort() is a function that sorts the list in ascending order
#items must be of the same type
list = ["ahmed","nasr","mohamed"]
list.sort()
print(list)#['ahmed', 'mohamed', 'nasr']
list = ["ahmed","nasr","mohamed"]
list.sort(reverse=True)
print(list)#['nasr', 'mohamed', 'ahmed']


#reverse() is a function that reverses the order of the list
list = ["ahmed","nasr","mohamed",4,5]
list.reverse()
print(list)#[5, 4, 'mohamed', 'nasr', 'ahmed']

#clear() is a function that removes all items from the list
list = ["ahmed","nasr","mohamed"]
list.clear()
print(list)#[]

#copy() is a function that returns a copy of the list
list = ["ahmed","nasr","mohamed"]
list2 = list.copy()
print(list2)#['ahmed', 'nasr', 'mohamed']
list2[0] = "khaled"
print(list2)#['khaled', 'nasr', 'mohamed']
print(list)#['ahmed', 'nasr', 'mohamed']


#count() is a function that returns the number of times an item appears in the list
list = ["ahmed","nasr","mohamed","ahmed"]
print(list.count("ahmed"))#2

#index() is a function that returns the index of the first occurrence of an item in the list
list = ["ahmed","nasr","mohamed"]
print(list.index("nasr"))#1

#pop() is a function that removes the item at the specified index
list = ["ahmed","nasr","mohamed"]
a=list.pop(0)
print(a)#ahmed
print(list)#['nasr', 'mohamed']
list = ["ahmed","nasr","mohamed"]
del list[0]
print(list)#['nasr', 'mohamed']

del list
print(list)#<class 'list'>