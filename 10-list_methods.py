#-------------
#List Methods
#-------------



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