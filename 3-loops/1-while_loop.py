#-------------
#Loops :while
#-------------
#while is a loop that executes a block of code as long as a condition is true
#Syntax
#while condition:
    #do something
#With the else statement we can run a block of code once when the condition no longer is true:
#else: 
    #do something
i = 1   #initialize the counter
while i <= 10: #condition
    print(i) #print the counter
    i += 1 #increment the counter
else:#when the condition is false
    print("i is no longer less than or equal to 10")    

names = ["ahmed","mohamed","ali"]
i = 0
while i < len(names):
    print(f"#{str(i+1).zfill(2)} {names[i]}")
    i += 1

#break : to exit the loop
names = ["ahmed","mohamed","ali"]
i = 0
while i < len(names):
    print(f"#{str(i+1).zfill(2)} {names[i]}")
    if names[i] == "mohamed":
        break
    i += 1

#continue : to skip the current iteration
names = ["ahmed","mohamed","ali"]
i = 0
while i < len(names):
    if names[i] == "mohamed":
        i += 1
        continue
    print(f"#{str(i+1).zfill(2)} {names[i]}")
    i += 1

#pass : to do nothing
names = ["ahmed","mohamed","ali"]
i = 0
while i < len(names):
    if names[i] == "mohamed":
        #implement something here
        pass
    print(f"#{str(i+1).zfill(2)} {names[i]}")
    i += 1