# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------
#pylint is a tool that checks for errors in Python code, enforces a coding standard, and looks for code smells. It can be used to improve the quality of your code and make it more readable.
#pylint.exe  file_name.py
#pylint will analyze the code in file_name.py and provide feedback on any issues it
"""
This is My Module
To Create Function
To Say Hello
"""

def say_hello(name):
  '''This Function Only Say Hello To Someone'''
  msg = "Hello"
  return f"{msg} {name}"

say_hello("Ahmed")