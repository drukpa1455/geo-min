# Getting Started
print("Hello, World!")

# Understanding Python's syntax and structure
# Basic program execution flow
# Interacting with the Python shell

# Basic Syntax
# Variables and assignments
my_variable = 10
print(my_variable)

# Naming conventions and best practices
# Variable types and dynamic typing
# Variable scope and lifetime

# Operators and expressions
a = 5
b = 3
sum = a + b
print(sum)

# Arithmetic operators
# Comparison and logical operators
# Operator precedence and associativity

# Conditional statements (if-else)
x = 10
if x > 0:
    print("Positive")
else:
    print("Non-positive")

# Syntax and usage
# Multiple conditions (if-elif-else)
# Conditional expressions (ternary operator)

# Variables and Data Types
# Numbers
x = 5
y = 2.5
z = complex(1, 2)
print(x, y, z)

# Integers, floats, and complex numbers
# Numeric operations and conversions

# Strings and string manipulation
message = "Hello, Python!"
print(message)

# String literals and escape sequences
# String methods and formatting
# Regular expressions (re module)

# Lists
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Creating and accessing lists
# List methods and slicing
# List comprehension

# Tuples
coordinates = (3, 4)
print(coordinates)

# Creating and accessing tuples
# Tuple packing and unpacking
# Immutable nature and use cases

# Dictionaries
person = {"name": "John", "age": 30}
print(person)

# Creating and accessing dictionaries
# Dictionary methods and operations
# Dictionary comprehension

# Sets
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Creating and manipulating sets
# Set operations (union, intersection, etc.)
# Set comprehension

# Control Flow
# Loops (for and while)
for i in range(5):
    print(i)

# Iterating over sequences and ranges
# Loop control statements (break and continue)
# Nested loops and loop-else construct

# Conditional statements (if-elif-else)
x = 5
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Combining conditions with logical operators
# Chained comparisons and short-circuiting
# Conditional expressions and the "in" operator

# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Defining functions
# Function syntax and structure
# Function arguments (positional, keyword, default)
# Variable-length arguments (*args, **kwargs)

# Function scope and namespaces
# Global and local variables
# Variable shadowing

# Return values and None
# Returning values from functions
# The None object and its significance

# Function documentation and docstrings
# Writing meaningful function documentation
# Using docstrings and accessing them

# Modules and Packages
import math

# Creating and importing modules
# Modular programming concepts
# Module structure and organization
# Importing modules and namespaces

# Package structure and importing
# Packaging Python code into modules and sub-packages
# Setting up package directories and files
# Importing from packages and sub-packages

# File I/O
# Reading and writing text files
file = open("example.txt", "w")
file.write("Hello, File!")
file.close()

# Opening and closing files
# Reading methods (read, readline, readlines)
# Writing methods (write, writelines)

# Working with file objects
# File modes and access permissions
# File position and seeking
# File handling best practices (with statement)

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handling specific exceptions
# Catching and handling specific error types
# Multiple except clauses and exception hierarchy

# Using try-except blocks
# Syntax and structure of try-except
# Handling multiple exceptions
# Handling and logging exceptions

# The finally clause
# Executing code regardless of exception occurrence
# Use cases for finally (resource cleanup)

# Object-Oriented Programming
# Classes and objects
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(circle.area())

# Defining classes and instantiating objects
# Class attributes and instance attributes
# The self parameter and instance methods

# Inheritance and polymorphism
# Creating derived classes and overriding methods
# Method resolution order (MRO)
# Polymorphism and duck typing

# Encapsulation and abstraction
# Access modifiers (public, private, protected)
# Getter and setter methods
# Abstract classes and interfaces

# Regular Expressions
import re

pattern = r"\d+"
matches = re.findall(pattern, "I have 2 apples and 3 oranges")
print(matches)

# Pattern matching with re module
# Regular expression syntax and patterns
# Matching and searching operations
# Grouping and capturing

# Regular expression modifiers
# Matching modes (case-insensitive, multiline, etc.)
# Anchors and boundary matchers
# Lookahead and lookbehind assertions

# Debugging
x = 5
print("Before breakpoint")
# Insert a breakpoint here
print("After breakpoint")
