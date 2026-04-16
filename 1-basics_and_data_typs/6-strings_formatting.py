#-------------
#Strings formatting old way
#-------------
#%s for string
#%d for number
#%f for float
name = "ahmed"
age = 20
ranke=10
#print("my name is " + name + " and i am " +age + " years old and my rank is " + ranke)
#TypeError: can only concatenate str (not "int") to str
#can solve this problem by type casting
#print("my name is " + name + " and i am " + str(age) + " years old and my rank is " + str(ranke))

######################################################
print("my name is %s and i am %d years old and my rank is %f" %(name,age,ranke))
#my name is ahmed and i am 20 years old and my rank is 10.000000

#to control the number of decimal places
print("my rank is %.2f" %ranke)
#my rank is 10.00

#to control the strings
myString="ahmed nasr"
print("my name is %s" %myString)#my name is ahmed naser
print("my name is %.5s" %myString)#my name is ahmed


#-------------
#Strings formatting nwe ways
#-------------

#format method
print("my name is {} and i am {} years old and my rank is {}".format(name,age,ranke))
#my name is ahmed and i am 20 years old and my rank is 10

#if you want to spaceafy typs
print("my name is {:.5s} and i am {:d} years old and my rank is {:.2f}".format(name,age,ranke))
#my name is ahmed and i am 20 years old and my rank is 10.00


#format mony
myMoney=1347834
print("my money is {:_}".format(myMoney))#1_347_834
print("my money is {:,}".format(myMoney))#1,347,834
print("my money is {:,d}".format(myMoney))#1,347,834
print("my money is {:,f}".format(myMoney))#1,347,834.000000
print("my money is {:,.2f}".format(myMoney))#1,347,834.00


#rearange items
a,b,c="one","two","three"
print("a:{},b:{},c:{}".format(a,b,c))#a:one,b:two,c:three
print("a:{a},b:{b},c:{c}".format(a=a,b=b,c=c))#a:one,b:two,c:three
print("a:{2},b:{1},c:{0}".format(a,b,c))#a:three,b:two,c:one
x,y,z=1,2,3
print("x:{x},y:{y},z:{z}".format(x=x,y=y,z=z))#x:1,y:2,z:3

print("x:{2},y:{1},z:{0}".format(x,y,z))#x:3,y:2,z:1
print("x:{2},y:{1},z:{0:.2f}".format(x,y,z))#x:3,y:2,z:1.00

##########################################################


# f-string
# name = "ahmed"
# age = 20
print(f"my name is {name:.3s} and i am {age} years old")#my name is ahmed and i am 20 years old
