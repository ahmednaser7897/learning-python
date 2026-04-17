# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------
print("-"*10+"Zip ex 1"+ "-"*10)
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}
ultimateList = zip(list1,list2, dict1)
print(ultimateList)#<zip object at 0x000001F163203A80>
for item in ultimateList:
  print(type(item))#<class 'tuple'> of values from iterables and if its dict it will take the keys only
  print(item)#ex:(1, 'A', 'Name')

print("-"*10+"Zip ex 2"+ "-"*10)
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

  print("List 1 Item =>", item1)
  print("List 2 Item =>", item2)
  print("Tuple 1 Item =>", item3)
  print("Dict 1 Key =>", item4, "Value =>", dict1[item4])

