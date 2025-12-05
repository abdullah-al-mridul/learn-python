'''
learn_py.py
This script demonstrates basic Python syntax and features.
Authored by: Abdullah Al Mridul
Inspired by: W3Schools Python Tutorial
'''

# importing modules
import sys
import random

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

# single value to multiple variables
x = y = z = "Orange"
print(x, y, z)

# unpacking a collection
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x, y, z)

# , vs +
print("Hello", "World!")
print("Hello" + "World!")

# global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# global keyword
x = "awesome"
def myfunc():
  global x
  x = "fantastic"   
myfunc()
print("Python is " + x)

# numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# random number
print(random.randrange(1, 10))

# details casting
a = int(1)   # x will be 1
b = int(2.8) # y will be 2
c = int("3") # z will be 3
d = float(1)     # x will be 1.0
e = float(2.8)   # y will be 2.8
f = float("3")   # z will be 3.0
g = float("4.2") # w will be 4.2
h = str("s1") # x will be 's1'
i = str(2)    # y will be '2'
j = str(3.0)  # z will be '3.0'
print(a, b, c, d, e, f, g, h, i, j)

# multile strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# string array indexing
a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])
print(a[-5:])

# check substring
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# upper and lower case
a = "Hello, World!"
print(a.upper())
print(a.lower())

# remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.lstrip()) # returns "Hello, World! "
print(a.rstrip()) # returns " Hello, World"

# split string and replace
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "Hello, World!" 
print(a.replace("H", "J")) # returns Jello, World!
print(a.replace("World", "Everyone")) # returns Hello, Everyone!

# F-string
name = "John"
age = 36
print(f"My name is {name} and I am {age}")

# operators
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)