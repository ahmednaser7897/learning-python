import os.path

books=[]
fileName='files_example.text'

class book:
    def __init__(self,name,id,quantity):
        self.name=name
        self.id=id
        self.quantity=quantity

def addBook():
    f=open(fileName,'a')
    print(" this is a function to insert a book\n")
    name=input("Pleas enter the book name : ")
    id=input("\n Pleas enter the book id : ")
    quantity=input("\n Pleas enter the book quantity : ")
    b=book(name,id,quantity)
    books.append(b)
    f.write("\n"+name+"\t"+id+"\t"+quantity)
    f.close()

#للتاكد من وجود هذا الكتاب في الليست و 
#اذا وجد في الليست اذا هو موجود ايضا في الفايل 
#فنستدعي الفانكسن التي تمسح سطر معين من فايل
def deleteBook():
    print(" This Is a Function To Delete a Book\n\n")
    id=input(" Pleas Enter The Id Of The Book You Want To Delete : ")
    flag =False
    bookN=''
    for i in books:
        if i.id==id:
           # print(i.id)
            books.remove(i)
            flag=True
            bookN=i.name
            break
    if flag:
        deleteLineFromAfile(id,bookN)
        print("the book has been deleted\n")
    else:
        print("The book is not found\n")
    print("****************************************\n")

# to Delete a Specific Line in a File:
# Open the file in read mode
# Read the files contents 
# Open the file in write mode
# Use a for loop to read each line and write it to the file
# When we reach the line we want to delete, skip it

def deleteLineFromAfile(id,name):
    f1=open(fileName,'r')
    l=f1.readlines()
    f1.close()
    f2=open(fileName,'w')
    for line in l:
        if line.find(name+"\t"+id)!=-1:
            #print("delete"+line)
            continue
        else:
            #print("add"+line)
            f2.write(line)
    f2.close()

#sort the list of objects by an attribute of this object
def sorteByName():
    newlist = sorted(books, key=lambda x: x.name, reverse=False)
    showBooks(newlist)

# search useing bs so we search in a sorted temb list(newList)
def searchByName():
    print("this is a function to search for a book\n")
    name=input(" pleas enter the book name : ")
    newList=sorted(books, key=lambda x: x.name[0], reverse=False)
    h=len(newList)
    l=0
    m=(h+l)/2
    flage=False
    while l<=h:
        m=int((h+l)/2)
        if newList[m].name==name:
            flage=True
            print(" The book name is : "+newList[m].name)
            print(" The book id is : "+newList[m].id)
            print(" The book quantity is : "+newList[m].quantity)
            break
        elif newList[m].name>name:
            h=m-1
        else :
            l=m+1
    if flage:{}
    else :
        print("The book is not found\n")
    print("****************************************\n")

def searchById():
    print("This Is a Function To Delete a Book\n")
    id=input(" Pleas Enter The Id Of The Book You Want To Delete : ")
    flage=False
    for i in books:
        if id==i.id:
            print(i.name+"\t\t"+i.id+"\t\t"+i.quantity)
            flage=True
            break
    if flage:{}
    else:
        print("The book is not found\n")
    print("****************************************\n")

def showBooks(books):
    print("Name\t\tID\t\tQuantity\n")
    for item in books:
        print(item.name+"\t\t"+item.id+"\t\t"+item.quantity)
    print("****************************************\n")

#get all books in file to the books list
def getBooksFromFileToList():
    f=open(fileName,'r')
    for line in f:
        l=line.split('\t')
        print(l)
        b=book(l[0],l[1],l[2].strip())
        books.append(b)
    f.close

#to check if file exist or not
if(os.path.exists(fileName)):
    getBooksFromFileToList()
    g='y'
    while g!='n':
        print("Enter number to do one of the next operation\n")
        print("1-Insert a book   ")
        print("2-Delete a book by id  ")
        print("3-Search a book by id  ")
        print("4-Search a book by name  ")
        print("5-Display all books sorted by name ")
        print("6-Display all books unsorted \n")
        x=input("the number is : ")
        print("\n****************************************\n")
        if x=='1':
            addBook()
        elif  x=='2':
            deleteBook()
        elif  x=='3':
            searchById()
        elif  x=='4':
            searchByName()
        elif  x=='5':
            sorteByName()
        elif  x=='6':
            showBooks(books)
        else:
            print("not Found")
        print("\n****************************************")
        g=input("Do you want another operation?(y/n)")
        print("****************************************\n")
else:
    print('file not exist')
#test data
# ahmed	1101	3600
# naser	1102	1490
# mohamed	1104	687
# I am Sabriel	1105	3100
# w	1	1
