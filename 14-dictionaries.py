#-------------
#Dictionaries
#-------------
# [1] Set items are enclosed in {}
# [2] Dictionaries is mutable => you can add or remove items
# [3] Dictionaries items are key-value pairs
# [4] Key has only immutable items (numbers, strings, tuples)
# [5] Keyis not unique but if you have same key it will override the last one
# [6] value can be any data type (numbers, strings, tuples, lists, dictionaries,set ,boolean, One more dictionary)
# [7] Dictionaries is not ordered( can not access by index)
# [8] Dictionaries access by key
########
    #Dictionaries are mutable
    #The Dictionary Itself is Mutable: You can add or remove items from a dictionary using methods like .add(), .remove(), and .update() without creating a new object.
########
#Dictionaries
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)#{'name': 'John', 'age': 36, 'country': 'Norway'}
user={
    "name":"John",
    "age":30,
     "age":40,
    "city":"New York",
   "skell":[1,2,3]
}
print(user)#{'name': 'John', 'age': 30, 'city': 'New York'}
print(len(user))#4
print(len(user["skell"]))#3
print(user["name"])#John
print(user["age"])#40
print(user["skell"])#[1, 2, 3]
print(user["skell"][1])#2
print(user["skell"][0])#1
print(user.get("age"))#40

#if key is not exist it will return None
print(user.get("country"))#None


#print dictionary keys
print(user.keys())#dict_keys(['name', 'age', 'city', 'skell'])
print(list(user.keys()))#['name', 'age', 'city', 'skell']
# print dictionary values
print(user.values())#dict_values(['John', 40, 'New York', [1, 2, 3]])
print(list(user.values()))#['John', 40, 'New York', [1, 2, 3]]
# print dictionary items
print(user.items())#dict_items([('name', 'John'), ('age', 40), ('city', 'New York'), ('skell', [1, 2, 3])])
print(list(user.items()))#[('name', 'John'), ('age', 40), ('city', 'New York'), ('skell', [1, 2, 3])]


#-------------
#Dictionaries Methods
#-------------

#clear() is a method that removes all items from the dictionary
user={
    "name":"John",
    "age":30,
   
}
user.clear()
print(user)#{}

#update() is a method that updates the dictionary with the items from another dictionary
user={
    "name":"John",
    "age":30,
   
}
user["city"]="New York"
user1={
    "work":"programmer",
    "date":2023
}
user.update(user1)
print(user)#{'name': 'John', 'age': 30, 'city': 'New York', 'work': 'programmer', 'date': 2023}


#copy() is a method that returns a copy of the dictionary
#this is shallow copy 
#this is not deep copy
#so when chane one it will not change the other
user={
    "name":"John",
    "age":30,
   
}
user1=user.copy()
user["name"]="ahmed"
print(user)#{'name': 'ahmed', 'age': 30}
print(user1)#{'name': 'John', 'age': 30}


#setdefault() is a method that returns the value of the key if it is in the dictionary, otherwise it returns the default value
user={
    "name":"John",
    "age":30,
   
}

user.setdefault("name","ahmed")
print(user)#{'name': 'John', 'age': 30}
user.setdefault("work","programmer")
print(user)#{'name': 'John', 'age': 30, 'work': 'programmer'}

#pop() is a method that removes the item with the specified key from the dictionary
#if key is not exist it will raise an error
user={
    "name":"John",
    "age":30,
    
    "city":"New York",

}
user.pop("name")
#user.pop("date") this will raise an error
print(user)#{'age': 30, 'city': 'New York'}

#popitem() is a method that removes the last item from the dictionary
user={
    "name":"John",
    "age":30,
    
    "city":"New York",

}
user.popitem()
print(user)#{'name': 'John', 'age': 30}


#fromkeys() is a method that creates a new dictionary with the specified keys and value
keys=["name","age","city"]
values="x"
user=dict.fromkeys(keys,values)
print(user)#{'name': 'x', 'age': 'x', 'city': 'x'}

#The del keyword removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)#{'brand': 'Ford', 'year': 1964}
del thisdict
#print(thisdict)#NameError: name 'thisdict' is not defined