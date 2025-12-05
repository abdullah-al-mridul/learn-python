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


# comparison operators
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# chain comparison
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

# logical operators
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# identity operators
x = ["apple", "banana"]
y = x
print(x is y)       # True
print(x is not y)   # False

# membership operators
x = ["apple", "banana"]
print("banana" in x)    # True
print("banana" not in x) # False

# precedence of operators
x = 5 + 3 * 2
print(x)
y = (5 + 3) * 2
print(y)

# list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# access list items
print(thislist[1])
print(thislist[-1])
print(thislist[1:3])
print(thislist[:2])
print(thislist[2:])
print(thislist[-3:-1])

# change list items
thislist[1] = "blackcurrant"
print(thislist)

# extend list
thislist.extend(["orange", "kiwi"])
print(thislist)

# append list
thislist.append("mango")
print(thislist)

# insert list
thislist.insert(1, "orange")
print(thislist)

# pop list item
thislist.pop()
print(thislist)

# loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# short list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist_two = [5, 10, 15, 20, 25]
thislist.sort()
thislist_two.sort()
print(thislist , thislist_two)

# copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# join list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# access tuple items
print(thistuple[1])

# unpack tuple
(apple, banana, cherry) = thistuple
print(apple)
print(banana)
print(cherry)

# dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# access dictionary items
print(thisdict["model"])

# change dictionary items
thisdict["year"] = 2018
print(thisdict)

# elif statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# match statement
x = 2
match x:
  case 1:
    print("x == 1")
  case 2:
    print("x == 2")
  case 3:
    print("x == 3")
  case _:
    print("x is not present")

# function
def my_function():
    print("Hello from a function")
my_function()