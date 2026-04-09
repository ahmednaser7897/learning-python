#-------------
#Strings functions
#-------------
#Strings are sequences of characters
#Strings are indexed
#Strings are ordered
#Strings are iterable
########
    #Strings are immutable
    #1-No Item Assignment: You cannot change a specific character by its index.
    #Attempting an operation like my_string[0] = 'a' will raise a TypeError.
    #2-New Object Creation: Any operation that appears to "change" a string—such as concatenation (+), replace(), or upper()—
    #actually creates and returns an entirely new string object rather than modifying the original one.
    #3-Variable Reassignment vs. Mutability: You can reassign a variable to a different string (e.g., s = "hello", then s = "world"),
    #but this only changes which object the variable points to; it does not change the original "hello" object itself.
########

#len() is a function that returns the length (int) of iterable
name = "ahmed nasr"
print(len(name))

# strip() rstrip() lstrip()
#  is a function that returns a copy of the string with the leading and trailing characters removed
#if the argument is not specified it is " "

name = " ahmed nasr "
print(name.strip())
print(name.rstrip())
print(name.lstrip())
#if the argument is specified it is the characters that are removed
name = "###ahmed nasr###"
print(name.strip("#"))
print(name.rstrip("#"))
print(name.lstrip("#"))

#capitalize() 
# is a function that returns a copy of the string 
# with the first character of each word 

name = "ahmed nasr #fsd"
print(name.capitalize())#Ahmed nasr #fsd

#title() 
# is a function that returns a copy of the string 
# with the first character of each word 
#and firs character after a number 
#capitalized
name = "ahmed nasr #fsd"
print(name.title())#Ahmed Nasr #Fsd

#zfill()
# is a function that returns a copy of the string
# that is filled with zeros on the left to reach the specified length
a="1"
b="11"
c="111"
print(a.zfill(3))# 001
print(b.zfill(3))# 011
print(c.zfill(3))# 111

#count()
# is a function that returns the number of times the substring occurs in the string
name = "ahmed nasr #fsd"
print(name.count("a"))
#upper()
# is a function that returns a copy of the string 
# with all the characters converted to uppercase
name = "Ahmed Nasr"
print(name.upper())#AHMED NASR
#lower()
# is a function that returns a copy of the string 
# with all the characters converted to lowercase
name = "Ahmed Nasr"
print(name.lower())#ahmed nasr


#split() rsplit()
# is a function that returns a list of strings 
# split by the separator by default is " "
name = "ahmed nasr is my name"
print(name.split())#['ahmed', 'nasr', 'is', 'my', 'name']
#max split splat is the number of splits and make the last in one item
name = "ahmed-nasr-is-my-name"
print(name.split("-",3))#['ahmed', 'nasr', 'is', 'my-name']
print(name.rsplit("-",3))#['ahmed-nasr', 'is', 'my', 'name']



#center
# is a function that make string with center in a length
# that we give and fill the string with the specified character
# if does not fill the string with the specified character default is " " 
name = "ahmed nasr"
print(name.center(20,"#"))######ahmed nasr#####


#count
# is a function that returns the number of times the substring occurs in the string
#it can take start and end
name = "ahmed nasr"
print(name.count("a"))#2
print(name.count("a",0,4))#1


#swapcase
# is a function that returns a copy of the string 
# with the case of each character swapped
name = "Ahmed Nasr"
print(name.swapcase())#aHMED nASR


#startswith
# is a function that returns True if the string starts with the specified prefix
#it can take start and end
name = "Ahmed Nasr Mohamed"
print(name.startswith("Ahmed"))#True
print(name.startswith("ahmed"))#False
print(name.startswith("Ahmed",0,5))#True
print(name.startswith("ahmed",0,4))#False

#endswith
# is a function that returns True if the string starts with the specified prefix
#it can take start and end
name = "Ahmed Nasr Mohamed"
print(name.endswith("Mohamed"))#True
print(name.endswith("mohamed"))#False
print(name.endswith("Mohamed",10,))#True
print(name.endswith("mohamed",10,))#False



#index()
# is a function that returns the index of the first occurrence of the substring
#it can take start and end
name = "Ahmed Nasr Mohamed"
print(name.index("Mohamed"))#10
#print(name.index("mohamed"))#ValueError: substring not found
print(name.index("Mohamed",10,))#10
#print(name.index("mohamed",10,))#ValueError: substring not found

#find
# is a function that returns the index of the first occurrence of the substring
#it can take start and end
name = "Ahmed Nasr Mohamed"
print(name.find("Mohamed"))#10
print(name.find("mohamed"))#-1 not error like index function
print(name.find("Mohamed",10,))#10
print(name.find("mohamed",10,))#-1 not error like index function


#rjust , ljust
# that we give and fill the string with the specified character
# if does not fill the string with the specified character default is " " 
name = "ahmed nasr"
print(name.rjust(20,"$"))# $$$$$$$$$$ahmed nasr
print(name.ljust(20,"$"))#ahmed nasr$$$$$$$$$$

#splitlines
# is a function that returns a list of strings 
# split by the separator by default is " "
name = "ahmed nasr is my name\nahmed nasr is my name\nahmed nasr is my name"
print(name.splitlines())#['ahmed nasr is my name', 'ahmed nasr is my name', 'ahmed nasr is my name']
print(name.splitlines(True))#['ahmed nasr is my name\n', 'ahmed nasr is my name\n', 'ahmed nasr is my name\n']


# expandtabs
# is a function that returns a copy of the string 
# with all the tab characters expanded using the specified number of spaces
name = "ahmed nasr\tahmed nasr\tahmed nasr"
print(name.expandtabs(30))#ahmed nasr    ahmed nasr    ahmed nasr


#is functions
print("Ahmned Naser".istitle())#True
print("Ahmned naser".istitle())#False
print("Ahmned Naser".isspace())#False
print(" ".isspace())#True
print("".isupper())#False
print("Ahmned Naser".isspace())#False
print("ahmned naser".islower())#True
print("Ahmned Naser".islower())#False
print("AHMNED NASER".isupper())#True
print("Ahmned Naser".isupper())#False
#isidentifier 
#check if the string is a valid identifier (variable name)
print("my_name".isidentifier())#True
print("myName".isidentifier())#True
print("my--name".isidentifier())#False

#isnumeric [0-9] only
print("123".isnumeric())#True
print("123a".isnumeric())#False

#isalpha [a-z] only
print("ahmed".isalpha())#True
print("ahmed1".isalpha())#False

#isalpha [a-z] and [0-9]
print("ahmed".isalnum())#True
print("ahmed1".isalnum())#False

#isdecimal [0-9] only
print("123".isdecimal())#True
print("123a".isdecimal())#False


#replace
# is a function that returns a copy of the string 
# with all occurrences of the old substring replaced with the new substring
name = "ahmed nasr ahmed"
print(name.replace("ahmed","mohamed" ,1))#mohamed nasr ahmed
print(name.replace("ahmed","mohamed"))#mohamed nasr mohamed

#join
# is a function that returns a string 
# that is a concatenation of the strings in the iterable
list = ["ahmed","nasr","mohamed"]
print(",".join(list))#ahmed,nasr,mohamed