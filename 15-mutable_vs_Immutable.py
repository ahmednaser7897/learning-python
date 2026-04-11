#-------------
#Mutable vs Immutable in Python
#-------------

# In Python, every data type is either Mutable or Immutable
# Understanding this difference is very important

# =============================================
# What does Mutable and Immutable mean?
# =============================================
# Mutable   => you CAN change the object after creation (same id in memory)
# Immutable => you CANNOT change the object after creation (new id in memory)

# =============================================
# Quick Reference Table
# =============================================
# | Data Type   | Mutable?   | Ordered? | Indexed? | Duplicates? |
# |-------------|------------|----------|----------|-------------|
# | int         | Immutable  | -        | -        | -           |
# | float       | Immutable  | -        | -        | -           |
# | bool        | Immutable  | -        | -        | -           |
# | str         | Immutable  | Yes      | Yes      | Yes         |
# | tuple       | Immutable  | Yes      | Yes      | Yes         |
# | frozenset   | Immutable  | No       | No       | No          |
# | list        | Mutable    | Yes      | Yes      | Yes         |
# | set         | Mutable    | No       | No       | No          |
# | dict        | Mutable    | No*      | By Key   | Keys: No    |
# * dict preserves insertion order since Python 3.7

print("=" * 60)
print("  Mutable vs Immutable in Python")
print("=" * 60)


# =============================================================
# [1] IMMUTABLE TYPES - Strings
# =============================================================
print("\n" + "=" * 60)
print("  [1] Strings are IMMUTABLE")
print("=" * 60)

# --- You CANNOT change a character by index ---
myString = "ahmed"
print(f"Original string: {myString}")#ahmed
print(f"ID before: {id(myString)}")

# myString[0] = "A"  # TypeError: 'str' object does not support item assignment

# --- Any "change" creates a NEW object ---
myString2 = myString.upper()
print(f"After upper(): {myString2}")#AHMED
print(f"Original still the same: {myString}")#ahmed
print(f"ID of original: {id(myString)}")
print(f"ID of new string: {id(myString2)}")
# => Different IDs! A new object was created

# --- Reassignment changes the variable, NOT the object ---
myString = "hello"
print(f"After reassignment: {myString}")#hello
print(f"ID after reassignment: {id(myString)}")
# => The ID changed because it points to a completely new object

# --- Concatenation also creates a new object ---
a = "hello"
print(f"ID of a: {id(a)}")
a = a + " world"
print(f"After concatenation: {a}")#hello world
print(f"ID of a after concatenation: {id(a)}")
# => Different ID! a new string was created

# --- replace() does NOT modify original ---
name = "ahmed nasr"
newName = name.replace("ahmed", "mohamed")
print(f"Original: {name}")#ahmed nasr
print(f"After replace: {newName}")#mohamed nasr
# => Original is unchanged


# =============================================================
# [2] IMMUTABLE TYPES - Tuples
# =============================================================
print("\n" + "=" * 60)
print("  [2] Tuples are IMMUTABLE")
print("=" * 60)

# --- You CANNOT change an item by index ---
myTuple = ("one", "two", "three")
print(f"Original tuple: {myTuple}")
print(f"ID: {id(myTuple)}")

# myTuple[0] = "ahmed"  # TypeError: 'tuple' object does not support item assignment

# --- You CANNOT add or remove items ---
# myTuple.append("four")  # AttributeError: 'tuple' object has no attribute 'append'
# del myTuple[0]           # TypeError: 'tuple' object doesn't support item deletion

# --- Concatenation creates a NEW tuple ---
myTuple2 = myTuple + ("four", "five")
print(f"After concatenation: {myTuple2}")#('one', 'two', 'three', 'four', 'five')
print(f"ID of original: {id(myTuple)}")
print(f"ID of new tuple: {id(myTuple2)}")
# => Different IDs! New object created

# --- BUT a tuple CAN contain mutable objects (like lists) ---
myTuple3 = ("ahmed", [1, 2, 3], "nasr")
print(f"Tuple with list inside: {myTuple3}")
# You can modify the list INSIDE the tuple
myTuple3[1].append(4)
print(f"After modifying the list inside: {myTuple3}")#('ahmed', [1, 2, 3, 4], 'nasr')
print(f"ID is still the same: {id(myTuple3)}")
# => The tuple itself did not change, but the list inside it did!
# => You CANNOT replace the list with something else:
# myTuple3[1] = [5, 6, 7]  # TypeError

# --- To "modify" a tuple, convert to list and back ---
myTuple = ("one", "two", "three")
tempList = list(myTuple)
tempList[0] = "NEW"
myTuple = tuple(tempList)
print(f"Modified tuple: {myTuple}")#('NEW', 'two', 'three')


# =============================================================
# [3] IMMUTABLE TYPES - Numbers (int, float, bool)
# =============================================================
print("\n" + "=" * 60)
print("  [3] Numbers (int, float, bool) are IMMUTABLE")
print("=" * 60)

x = 10
print(f"x = {x}, ID: {id(x)}")
x = x + 5
print(f"x = {x}, ID: {id(x)}")
# => ID changed! x now points to a new int object (15)
# => The original int object (10) was NOT modified

y = 3.14
print(f"y = {y}, ID: {id(y)}")
y = y + 1
print(f"y = {y}, ID: {id(y)}")
# => Same thing with floats - new object created

z = True
print(f"z = {z}, ID: {id(z)}")
z = False
print(f"z = {z}, ID: {id(z)}")
# => Booleans are also immutable


# =============================================================
# [4] MUTABLE TYPES - Lists
# =============================================================
print("\n" + "=" * 60)
print("  [4] Lists are MUTABLE")
print("=" * 60)

# --- You CAN change items by index ---
myList = ["ahmed", "nasr", "mohamed"]
print(f"Original list: {myList}")
print(f"ID before: {id(myList)}")

myList[0] = "khaled"
print(f"After changing index 0: {myList}")#['khaled', 'nasr', 'mohamed']
print(f"ID after: {id(myList)}")
# => SAME ID! The list was modified in place

# --- You CAN add items ---
myList.append("sayed")
print(f"After append: {myList}")#['khaled', 'nasr', 'mohamed', 'sayed']
print(f"ID still same: {id(myList)}")
# => SAME ID!

# --- You CAN remove items ---
myList.remove("sayed")
print(f"After remove: {myList}")#['khaled', 'nasr', 'mohamed']
print(f"ID still same: {id(myList)}")
# => SAME ID!

# --- sort() and reverse() modify in place ---
myList2 = [3, 1, 4, 1, 5, 9]
print(f"Before sort: {myList2}, ID: {id(myList2)}")
myList2.sort()
print(f"After sort: {myList2}, ID: {id(myList2)}")
# => SAME ID! sort() modifies the list directly

# --- Slice Assignment ---
myList3 = [1, 2, 3, 4, 5]
print(f"Before slice assignment: {myList3}")
myList3[1:3] = [20, 30]
print(f"After slice assignment: {myList3}")#[1, 20, 30, 4, 5]
print(f"ID still same: {id(myList3)}")
# => SAME ID!


# =============================================================
# [5] MUTABLE TYPES - Sets
# =============================================================
print("\n" + "=" * 60)
print("  [5] Sets are MUTABLE")
print("=" * 60)

# --- You CAN add items ---
mySet = {"ahmed", "nasr", "mohamed"}
print(f"Original set: {mySet}")
print(f"ID before: {id(mySet)}")

mySet.add("sayed")
print(f"After add: {mySet}")
print(f"ID after: {id(mySet)}")
# => SAME ID! The set was modified in place

# --- You CAN remove items ---
mySet.discard("sayed")
print(f"After discard: {mySet}")
print(f"ID still same: {id(mySet)}")
# => SAME ID!

# --- update() modifies in place ---
mySet.update({1, 2, 3})
print(f"After update: {mySet}")
print(f"ID still same: {id(mySet)}")
# => SAME ID!

# --- BUT set items must be IMMUTABLE ---
# mySet.add([1, 2, 3])     # TypeError: unhashable type: 'list'
# mySet.add({"a": 1})       # TypeError: unhashable type: 'dict'
mySet.add((1, 2, 3))         # OK! tuples are immutable
print(f"After adding tuple: {mySet}")

# --- frozenset is the IMMUTABLE version of set ---
myFrozenSet = frozenset({"ahmed", "nasr", "mohamed"})
print(f"Frozenset: {myFrozenSet}")
# myFrozenSet.add("sayed")  # AttributeError: 'frozenset' object has no attribute 'add'


# =============================================================
# [6] MUTABLE TYPES - Dictionaries
# =============================================================
print("\n" + "=" * 60)
print("  [6] Dictionaries are MUTABLE")
print("=" * 60)

# --- You CAN change values ---
myDict = {"name": "ahmed", "age": 25, "city": "Cairo"}
print(f"Original dict: {myDict}")
print(f"ID before: {id(myDict)}")

myDict["name"] = "mohamed"
print(f"After changing name: {myDict}")
print(f"ID after: {id(myDict)}")
# => SAME ID! Modified in place

# --- You CAN add new key-value pairs ---
myDict["job"] = "developer"
print(f"After adding key: {myDict}")
print(f"ID still same: {id(myDict)}")
# => SAME ID!

# --- You CAN remove items ---
myDict.pop("city")
print(f"After pop: {myDict}")
print(f"ID still same: {id(myDict)}")
# => SAME ID!

# --- BUT keys must be IMMUTABLE ---
# myDict[[1,2]] = "test"    # TypeError: unhashable type: 'list'
myDict[(1, 2)] = "test"      # OK! tuples are immutable
print(f"Dict with tuple key: {myDict}")


# =============================================================
# [7] KEY DIFFERENCE: Assignment vs Modification
# =============================================================
print("\n" + "=" * 60)
print("  [7] Assignment vs Modification (Very Important!)")
print("=" * 60)

# --- With MUTABLE types (list) => both variables see the change ---
print("\n--- Mutable (List) ---")
listA = [1, 2, 3]
listB = listA  # Both point to the SAME object
print(f"listA: {listA}, ID: {id(listA)}")
print(f"listB: {listB}, ID: {id(listB)}")
# => Same ID!

listA.append(4)
print(f"After listA.append(4):")
print(f"listA: {listA}")#[1, 2, 3, 4]
print(f"listB: {listB}")#[1, 2, 3, 4]
# => Both changed! Because they point to the same object

# --- With IMMUTABLE types (string) => only one variable changes ---
print("\n--- Immutable (String) ---")
strA = "hello"
strB = strA  # Both point to the SAME object
print(f"strA: {strA}, ID: {id(strA)}")
print(f"strB: {strB}, ID: {id(strB)}")

strA = strA + " world"  # Creates a NEW object
print(f"After strA = strA + ' world':")
print(f"strA: {strA}")#hello world
print(f"strB: {strB}")#hello  => did NOT change!
print(f"strA ID: {id(strA)}")
print(f"strB ID: {id(strB)}")
# => Different IDs! strA points to new object, strB still points to old one

# --- With IMMUTABLE types (tuple) => only one variable changes ---
print("\n--- Immutable (Tuple) ---")
tupleA = (1, 2, 3)
tupleB = tupleA
print(f"tupleA: {tupleA}, ID: {id(tupleA)}")
print(f"tupleB: {tupleB}, ID: {id(tupleB)}")

tupleA = tupleA + (4,)
print(f"After tupleA = tupleA + (4,):")
print(f"tupleA: {tupleA}")#(1, 2, 3, 4)
print(f"tupleB: {tupleB}")#(1, 2, 3) => did NOT change!


# =============================================================
# [8] How to safely copy MUTABLE objects
# =============================================================
print("\n" + "=" * 60)
print("  [8] How to Safely Copy Mutable Objects")
print("=" * 60)

# --- WRONG way (both point to same object) ---
print("\n--- Wrong way (no copy) ---")
original = [1, 2, 3]
wrong_copy = original
wrong_copy.append(4)
print(f"original: {original}")#[1, 2, 3, 4] => changed!
print(f"wrong_copy: {wrong_copy}")#[1, 2, 3, 4]

# --- RIGHT way using .copy() ---
print("\n--- Right way using .copy() ---")
original = [1, 2, 3]
right_copy = original.copy()
right_copy.append(4)
print(f"original: {original}")#[1, 2, 3] => did NOT change!
print(f"right_copy: {right_copy}")#[1, 2, 3, 4]

# --- RIGHT way using slicing ---
print("\n--- Right way using slicing ---")
original = [1, 2, 3]
right_copy2 = original[:]
right_copy2.append(4)
print(f"original: {original}")#[1, 2, 3] => did NOT change!
print(f"right_copy2: {right_copy2}")#[1, 2, 3, 4]

# --- Same for dictionaries ---
print("\n--- Copy dictionary ---")
originalDict = {"name": "ahmed", "age": 25}
dictCopy = originalDict.copy()
dictCopy["name"] = "mohamed"
print(f"originalDict: {originalDict}")#{'name': 'ahmed', 'age': 25} => did NOT change!
print(f"dictCopy: {dictCopy}")#{'name': 'mohamed', 'age': 25}

# --- Same for sets ---
print("\n--- Copy set ---")
originalSet = {1, 2, 3}
setCopy = originalSet.copy()
setCopy.add(4)
print(f"originalSet: {originalSet}")#{1, 2, 3} => did NOT change!
print(f"setCopy: {setCopy}")#{1, 2, 3, 4}


# =============================================================
# [9] COMPARISON SUMMARY
# =============================================================
print("\n" + "=" * 60)
print("  [9] Final Comparison Summary")
print("=" * 60)

# --- Immutable types ---
print("\n--- Immutable Types ---")
print("String:    Cannot change characters, methods return NEW strings")
print("Tuple:     Cannot add/remove/change items, concatenation creates NEW tuple")
print("int/float: Cannot change value, operations create NEW numbers")
print("frozenset: Cannot add/remove items, like an immutable set")
print("bool:      Cannot change value")

# --- Mutable types ---
print("\n--- Mutable Types ---")
print("List:       Can change/add/remove items, methods modify IN PLACE")
print("Set:        Can add/remove items, methods modify IN PLACE")
print("Dictionary: Can change/add/remove key-value pairs, methods modify IN PLACE")

# --- Practical tips ---
print("\n--- Practical Tips ---")
print("1. Use .copy() or [:] to avoid unexpected changes when sharing mutable objects")
print("2. Tuples are safer than lists when you don't need to change the data")
print("3. Only immutable types can be used as dictionary keys or set items")
print("4. Use id() to check if two variables point to the same object")
print("5. Strings look like they change but they always create a new object")
