#---------------------------------------------------------
#python basic of file handling
#---------------------------------------------------------
# "a" Append mode to add content to the end of the file (will create the file if it does not exist)
# "r" Read [default] mode to read the file (will raise an error if the file does not exist)
# "w" Write mode to write to the file (will create the file if it does not exist)
# "x" Create mode to create a new file (will raise an error if the file already exists)

# to open a file we use the open() function
# the open() function takes two arguments: the file name and the mode
# the open() function returns a file object that we can use to read or write to the file
#file=open("myfile.txt")#this will raise an error if the file does not exist
#file=open("myfile.txt","r")#this will raise an error if the file does not exist
#file=open(r"myfile.txt","w")#this will create the file if it does not exist

#------------------------
#file read
#------------------------
#test data
# hello world1
# hello world2
# hello world3
# Ahmed Naser
# Mohmed Naser
# Mahmoud Naser
# Khalid Sayed
file=open(r"myfile.txt","r")
# the file object has several attributes that we can use to get information about the file
# print(file)#<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>
# print(file.name)#myfile.txt
# print(file.mode)#w
# print(file.encoding)#cp1252


#print(file.read())#this will read the entire file and return it as a string
# print("-"*50)
# print(file.read(5))#this will read the first 5 characters of the file
# print("-"*50)
# print(file.readline())#this will read the first line of the file
# print(file.readlines(3))#this will read the first 3 lines of the file
# print(file.readlines())#this will read all the lines of the file

# for line in file:
#     print(line,end="")#this will read the file line by line and print it to the console

file.close()



#------------------------
#file Write
#------------------------
file=open(r"myfile2.txt","w")#this will create the file if it does not exist
#file.write removes the existing content of the file and writes the new content to the file
file.write("Hello World1\n")#this will write the string to the file
file.write("Hello World2\n")#this will write the string to the file
myList=["Hello World3\n","Ahmed Naser\n","Mohmed Naser\n","Mahmoud Naser\n","Khalid Sayed\n"]
file.writelines(myList)#this will write the list of strings to the file
file.close()

#------------------------
#file Append
#------------------------
# file=open(r"myfile3.txt","a")#this will create the file if it does not exist
# #file.write will add the new content to the end of the file
# file.write("Hello World4\n")#this will write the string to the file
# file.close()


#------------------------
#file functions
#------------------------
file=open(r"myfile3.txt","a")#this will create the file if it does not exist
#file.truncate(5)#this will remove the content of the file from the 5th character to the end of the file
print(file.tell())#this will return the current position of the file pointer
file.seek(0)#this will move the file pointer to the beginning of the file
print(file.tell())
file.seek(5)#this will move the file pointer to the 5th character of the file
print(file.tell())
file.write("Hello World4\n")#this will write the string to the file
file.close()