'''
learn_py.py
This script demonstrates basic Python syntax and features.
Authored by: Abdullah Al Mridul
Inspired by: W3Schools Python Tutorial
'''

# importing sys module
import sys

# if statement
if 10 > 8:
    print(sys.version)
    print("Hello, World!")

# variable assignment
x = 5
y = "John"
print(x, y)

# python statement
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

# semicolons
a = 5; b = 10; print(a + b)

# quotes
single_quote = 'Hello'
double_quote = "World"
print(single_quote, double_quote)

# print without newline
print("Hello" , end=" "); print("World!")

# number
print(7)
print(3.14)
print(2 + 3)

# number and string combination
print("The number is", 7 , "and the string is", "Python")

# casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

# get the type
print(type(x))
print(type(y))
print(type(z))

# case sensitivity
a = 4
A = "Sally"
print(a , A)

# variable naming rules
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

# multiple assignments
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)