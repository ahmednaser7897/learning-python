# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

def user_data():
    try:# Try The Code and Test Errors
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        print(f"Hello {name}, You Are {age} Years Old")
    except : # Handle The Errors If Its Found
        print("Invalid input. Please enter a valid number.")
    else: # If No Errors Found
        print("Data Processed Successfully.")
    finally: # Run The Code Always
        print("Thank You For Using Our Service.")
user_data()  

def division(value1, value2):
    try:
        result = value1 / value2
        print(f"The Result Of {value1} / {value2} Is: {result}")
    except ZeroDivisionError: # Handle The ZeroDivisionError If Its Found
        print("You Can't Divide By Zero.")
    except ValueError: # Handle The ValueError If Its Found
        print("Invalid input. Please enter a valid number.")
    except TypeError: # Handle The TypeError If Its Found
        print("Invalid input. Please enter a valid number.")
    except Exception as e: # Handle Any Other Errors If Its Found
        print(f"An error occurred: {e}")
    else: # If No Errors Found
        print("Division Performed Successfully.")
    finally: # Run The Code Always
        print("Thank You For Using Our Service.")       
division(10, 2) #The Result Of 10 / 2 Is: 5.0, Division Performed Successfully., Thank You For Using Our Service.
print("-"*30)
division(10, 0) #You Can't Divide By Zero., Thank You For Using Our
print("-"*30)
division(10, "a") #Invalid input. Please enter a valid number., Thank You For Using Our Service.
print("-"*30)

print("-"*10+"Example"+ "-"*10)
#the file name :9-errors_and_exceptions\test.txt
def open_file():
    tryes=5
    my_file=None
    while tryes>0:
        try:
            print(f"You Have {tryes} Tryes Left.")
            file_name = input("Enter The File Name: ")
            my_file = open(file_name, "r")
            print(my_file.read())
            break
        except FileNotFoundError:
            print("An error occurred while opening the file.")
            tryes-=1
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if my_file:
                my_file.close()
            print("Thank You For Using Our Service.")   
    else:
        print("You Have Tried 5 Times, Please Try Again Later.")
   

open_file()