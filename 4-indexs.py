#paython is a zero based language
# we can use index to access the elements of a list or string
name = "ahmed naser"
#normal index starts from 0
print(name[0])# a
#negative index starts from -1
print(name[-1])# r

#Slicing (Accessing a range of elements)
#[start:end] end is not included
#[start:end:step]
print(name[0:4])# ahme
#if start is not specified it is 0
print(name[:4])# ahme
#if end is not specified it is the length of the string
print(name[4:])# d naser
#if start and end are not specified it is the whole string
print(name[:])# ahmed naser
#if step is not specified it is 1
print(name[1:9:2])# he a
