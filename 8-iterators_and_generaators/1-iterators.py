# -------------------------------
# ---Iterables vs Iterators -----
# -------------------------------
# ---Iterables:---
# [1] object contains data that can be iterated over (e.g., list, tuple, string, set, dictionary)
# [2] can be used in a for loop or with the iter() function to create an iterator
# [3] can be converted to an iterator using the iter() function
# ---Iterators:---
# [1] object used to iterate over an iterable using the next() function returns the next item in the sequence
# [2] ypically created using the iter() function on an iterable
# [3] for loop automatically creates an iterator from the iterable and uses it to iterate over the items
# [4] once an iterator is exhausted (no more items to return), it raises a StopIteration exception
# -----------------------------------------------------------------------------------

# Example of an normal iterable (list)
print("-"*10+"normal iterable"+ "-"*10)
my_string = "Hello"
#the loop adds an implicit call to iter() to create an iterator from the string, 
# and then uses next() to get each character until the string is exhausted.
my_string = "Hello"
for char in iter(my_string):
    print(char, end="-")  # Output: H-e-l-l-o- (each character followed by an underscore)
print()
#the same like this
for char in my_string:
    print(char, end="-")  # Output: H-e-l-l-o- (each character followed by an underscore)
print()



# Example of an iterator
print("-"*10+"iterator"+ "-"*10)
my_string = "Hello"
#print(next(my_string)) #error TypeError: 'str' object is not an iterator
#to convert iterable to iterator use iter() function
my_string = "Hello World"
my_string_iterator = iter(my_string)
print(next(my_string_iterator)) #H
print(next(my_string_iterator)) #e
print(next(my_string_iterator)) #l
#The next() function is used to retrieve the next value from the iterator.
#Each time next() is called, it returns the next value in the sequence defined by the generator function.
# When there are no more values to return, it raises a StopIteration exception.
#So this will print 4, 5, 6 because the generator function my_iterator() yields those values in sequence, 
# and we are calling next() on the iterator created from that generator.
for num in my_string_iterator:
    print(num, end=" ") #l, o,  , W, o, r, l, d (each character of the string "Hello World" printed on a new line)
print()
#When the for loop is used to iterate over an iterator, 
#It automatically handles the StopIteration exception when the iterator is exhausted, 
#So we don't need to worry about it in this case.
#print(next(my_string_iterator)) #error StopIteration: because the iterator is exhausted (no more items to return) and raises a StopIteration exception.

