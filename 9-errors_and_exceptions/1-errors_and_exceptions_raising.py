# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

print("-"*10+"Normal Function with no errors"+ "-"*10)
def check_number(num):
    if num > 0:
        return f"{num} is a valid number"
    elif num == 0:
        return "Zero is not allowed"
    else:
        return f"{num} is not a valid number"
print(check_number(5)) #5 is a valid number
print(check_number(0)) #Zero is not allowed
print(check_number(-5)) #-5 is not a valid number
# raise Exception("x Should Not Be Larger Than 5")


# To Raise Your Own Exceptions You Can Use The raise Keyword Followed By
#  The Exception You Want To Raise
print("-"*10+"raise my own exceptions"+ "-"*10)
def check_number(num):
    if num > 0:
        return f"{num} is a valid number"
    elif num == 0:
        raise Exception("Zero is not allowed")
    else:
        raise Exception(f"{num} is not a valid number")
    
print(check_number(5)) #5 is a valid number
#print(check_number(0)) #Exception: Zero is not allowed
#print(check_number(-5)) #Exception: -5 is not a valid number

def check_number(num):
    if num > 0:
        return f"{num} is a valid number"
    elif num == 0:
        raise ValueError("Zero is not allowed")
    else:
        raise ValueError(f"{num} is not a valid number")
    
print(check_number(5)) #5 is a valid number
#print(check_number(0)) #ValueError: Zero is not allowed
#print(check_number(-5)) #ValueError: -5 is not a valid number