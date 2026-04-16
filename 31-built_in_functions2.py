# -------------------------------
# --- Python functions->>Map ----
# -------------------------------
# [1] Map take a function and an iterable
# [2] Map returns an iterator that applies the function to every item of the iterable
# [3] the function can be predefined or lambda function
# -----------------------------------------------------------------------------------

print("-"*10+"Map function"+ "-"*10)
def format_name(name):
    return f"- {name.title().strip()} -"

print(format_name("ahmed"))#- Ahmed -
my_list = ["Ahmed", " moHamEd", "aLi", "sayed ", "KHALED "]

#map(function, iterable) function applies the function to every item of the iterable and returns an iterator
formatted_list = map(format_name, my_list)
print(formatted_list) #<map object at 0x7f8c8c8c8c8c>
print(list(formatted_list))#['- Ahmed -', '- Mohamed -', '- Ali -', '- Sayed -', '- Khaled -']


#WITH LAMBDA FUNCTION
print("-"*10+"Map with lambda function"+ "-"*10)
formatted_list = map(lambda name: f"- {name.title().strip()} -", my_list)
print(list(formatted_list))#['- Ahmed -', '- Mohamed -', '- Ali -', '- Sayed -', '- Khaled -']
for name in map(lambda name: f"- {name.title().strip()} -", my_list):
    print(name)


# -------------------------------
# --- Python functions->>Filter ----
# -------------------------------
# [1] Filter take a function and an iterable
# [2] Filter returns an iterator that applies the function to every item of the iterable
# [3] The function can be predefined or lambda function
# [4] The function must return a boolean value (True or False)
# [5] Filter only returns the items that the function returns True for
# -----------------------------------------------------------------------------------


print("-"*10+"Filter function"+ "-"*10)
def is_even(num):
    return num % 2 == 0
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, my_numbers)
print(even_numbers) #<filter object at 0x7f8c8c8c8c8c>
print(list(even_numbers)) #[2, 4, 6, 8, 10]
for num in filter(is_even, my_numbers):
    print(num,end="-") #2-4-6-8-10-
print() #for new line 
#WITH LAMBDA FUNCTION
print("-"*10+"Map with lambda function"+ "-"*10)

my_names = ["Ahmed", " moHamEd", "ALi", "sayed ", "KHALED "]
even_names = filter(lambda name: name.startswith("A"), my_names)
print(list(even_names))#['Ahmed', 'ALi']


# ----------------------------------
# --- Python functions->>Reduce ----
# ----------------------------------
# [1] Reduce take a function and an iterable
# [2] Reduce run a function on the first two items of the iterable and  give result 
#     and the next item to the function and so on 
#     until the iterable is exhausted and returns a single value
# [3] The function can be predefined or lambda function
# -----------------------------------------------------------------------------------
print("-"*10+"Reduce function"+ "-"*10)
from functools import reduce
def sum_numbers(num1,num2):
    return num1+num2
my_numbers = [1, 2, 3, 4, 5,]
result = reduce(sum_numbers, my_numbers)
print(result) #15-->1+2+3+4+5-->(1+2)+3+4+5-->(3)+3+4+5-->(6)+4+5-->(10)+5-->15
#WITH LAMBDA FUNCTION
result = reduce(lambda num1,num2: num1+num2, my_numbers)
print(result) #15