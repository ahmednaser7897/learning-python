# -------------------------
# --- Python functions ----
# -------------------------
# all()
# any()
# bin()
# id()

# all(iterable) function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable is empty, it returns True.
print("-"*10+"all() function"+ "-"*10)
x = [1, 2, 3, 4]
print(all(x))  # True
y = [1, 0, 3, 4]
print(all(y))  # False
z=[]
print(all(z))  # True

# any(iterable) function returns True if any item in an iterable is true, otherwise it returns False.
# If the iterable is empty, it returns False.
print("-"*10+"any() function"+ "-"*10)
x = [0, 0, 0, 0]
print(any(x))  # False
y = [1, 0, 3, 4]
print(any(y))  # True
z=[]
print(any(z))  # False

# bin(x) function returns the binary representation of an integer.
print("-"*10+"bin() function"+ "-"*10)
x = 10
print(bin(x))  # 0b1010

# id(x) function returns the identity of an object.
print("-"*10+"id() function"+ "-"*10)
x = 10
print(id(x))  # 140711799863216 (this will be different every time you run the code)
y = x
print(id(y))  # 140711799863216 (this will be the same as x because y is referencing the same object as x)
z = 10
print(id(z))  # 140711799863216 (this will be the same as x and y because small integers are cached by Python and all references to the same small integer will point to the same object in memory)

# -------------------------
# --- Python functions ----
# -------------------------
# sum()
# round()
# range()
# print()

# sum(iterable, start) function returns the sum of all items in an iterable.
print("-"*10+"sum() function"+ "-"*10)
x = [1, 2, 3, 4]
print(sum(x))  # 10
print(sum(x, 5))  # 15--->sum of all items in x + 5

# round(number, ndigits) function returns the number rounded to ndigits precision after the decimal point.
print("-"*10+"round() function"+ "-"*10)
x = 3.14159
print(round(x))  # 3
print(round(x, 2))  # 3.14
print(round(x, 4))  # 3.1416


# range(start, stop, step) function returns a sequence of numbers.
print("-"*10+"range() function"+ "-"*10)
x = range(5)
print(x)  # range(0, 5)
print(list(x))  # [0, 1, 2, 3, 4]
x = range(2, 5)
print(x)  # range(2, 5)
print(list(x))  # [2, 3, 4]
x = range(2, 10, 2)
print(x)  # range(2, 10, 2)
print(list(x))  # [2, 4, 6, 8]

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) 
# function prints the objects to the console.
print("-"*10+"print() function"+ "-"*10)
print("Hello", "World",)  # Hello World
print("Hello", "World", sep="-")  # Hello-World
print("Hello", "World", end="!")  # Hello World!

# -------------------------
# --- Python functions ----
# -------------------------
# abs()
# pow()
# min()
# max()
# slice()

# abs(x) function returns the absolute value of x.
print("-"*10+"abs() function"+ "-"*10)
x = -10
print(abs(x))  # 10
x = 10
print(abs(x))  # 10

# pow(base, exponent, modulus) function returns the value of base raised to the power of exponent.
print("-"*10+"pow() function"+ "-"*10)
x = 2
y = 3
print(pow(x, y))  # 8
print(pow(x, y, 5))  # 3 (equivalent to (2**3) % 5) modulus is 5
# min(iterable) function returns the smallest item in an iterable.
print("-"*10+"min() function"+ "-"*10)
x = [1, 2, 3, 4]
print(min(x))  # 1

# max(iterable) function returns the largest item in an iterable.
print("-"*10+"max() function"+ "-"*10)
x = [1, 2, 3, 4]
print(max(x))  # 4

# slice(start, stop, step) function returns a slice object that can be used to slice a sequence.
print("-"*10+"slice() function"+ "-"*10)
x = "Hello World"
s = slice(0, 5)
print(x[s])  # Hello->>slice the string from index 0 to index 5 (not including index 5)
s = slice(6, 11)
print(x[s])  # World -->x[6:11] slice the string from index 6 to index 11 (not including index 11)
s = slice(0, 11, 2)
print(x[s])  # HloWrd -->x[0:11:2] slice the string from index 0 to index 11 (not including index 11) with a step of 2 (skip every other character)


# -------------------------
# --- Python functions ----
# -------------------------
# enumerate()
# help()
# reversed()

# enumerate(iterable, start=0) function returns an enumerate object that can be used to iterate over a sequence.
print("-"*10+"enumerate() function"+ "-"*10)
x = ["apple", "banana", "cherry"]
enumerate_x=enumerate(x)
print(enumerate_x)  # <enumerate object at 0x7f8c5c4b8f60>
for counter, item in enumerate_x:
    print(counter, item)

# help(function) function returns the documentation string of a function.
print("-"*10+"help() function"+ "-"*10)
help(print)

# reversed(sequence) function returns a reversed iterator that can be used to iterate over a sequence in reverse order.
print("-"*10+"reversed() function"+ "-"*10)
x = [1, 2, 3, 4]
reversed_x = reversed(x)
print(reversed_x)  # <list_reverseiterator object at 0x7f8c5c4b8f60>
print(list(reversed_x))  # [4, 3, 2, 1]
