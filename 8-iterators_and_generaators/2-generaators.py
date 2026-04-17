# -------------------------------
# ---Generators -----
# -------------------------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------
print("-"*10+"Generator"+ "-"*10)
def my_iterator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
my_iterator_list =my_iterator() 
print(my_iterator_list) #<generator object my_iterator at 0x000001B2F8C9B0D0>
print(next(my_iterator_list)) #1
print(next(my_iterator_list)) #2
print(next(my_iterator_list)) #3
#The next() function is used to retrieve the next value from the iterator.
#Each time next() is called, it returns the next value in the sequence defined by the generator function.
# When there are no more values to return, it raises a StopIteration exception.
#So this will print 4, 5, 6 because the generator function my_iterator() yields those values in sequence, 
# and we are calling next() on the iterator created from that generator.
for num in my_iterator_list:
    print(num,end=" ") #4, 5, 6
print()
#When the for loop is used to iterate over an iterator, 
#It automatically handles the StopIteration exception when the iterator is exhausted, 
#So we don't need to worry about it in this case.
#print(next(my_iterator_list)) #error StopIteration: because the iterator is exhausted (no more items to return) and raises a StopIteration exception.
