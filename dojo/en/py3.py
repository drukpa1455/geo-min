import math
import os
import io
import datetime
import json

# Library Reference
# Built-in Functions
## Mathematical functions (math module)
sqrt_result = math.sqrt(16)
print("Square root of 16:", sqrt_result)

## String functions and methods
string_length = len("Hello, world!")
print("Length of the string:", string_length)

## File and I/O functions (os, io modules)
file_path = "example.txt"
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")

with open("example.txt", "r") as file:
    file_contents = file.read()
    print("File contents:", file_contents)

# Built-in Types
## Numeric types (int, float, complex)
num = 42
float_num = float(num)
print("Floating point number:", float_num)

### Numeric operations and built-in functions
absolute_value = abs(-10)
print("Absolute value:", absolute_value)

### Numeric type conversions and formatting
hex_value = hex(255)
print("Hexadecimal value:", hex_value)

## Sequence types (list, tuple, range)
my_list = [1, 2, 3]
list_length = len(my_list)
print("Length of the list:", list_length)

### Sequence operations and methods
my_tuple = (4, 5, 6)
tuple_sum = sum(my_tuple)
print("Sum of the tuple:", tuple_sum)

### List and tuple manipulation techniques
my_list.append(4)
print("Modified list:", my_list)

## Mapping types (dict)
my_dict = {"name": "John", "age": 25}
dict_keys = my_dict.keys()
print("Dictionary keys:", dict_keys)

### Dictionary operations and methods
my_dict["occupation"] = "Engineer"
print("Modified dictionary:", my_dict)

### Dictionary iteration and comprehension
for key, value in my_dict.items():
    print(key, ":", value)

## Set types (set, frozenset)
my_set = {1, 2, 3}
set_length = len(my_set)
print("Length of the set:", set_length)

### Set operations and methods
my_set.add(4)
print("Modified set:", my_set)

### Set algebra and membership testing
set_intersection = {2, 3, 4} & {3, 4, 5}
print("Intersection of sets:", set_intersection)

# Standard Library Modules
## os module for operating system interactions
### File and directory manipulation
file_size = os.path.getsize("example.txt")
print("File size:", file_size)

### Environment variables and process handling
current_working_directory = os.getcwd()
print("Current working directory:", current_working_directory)

## datetime module for date and time manipulation
### Date and time objects and operations
current_date = datetime.date.today()
print("Current date:", current_date)

### Formatting and parsing date/time strings
date_string = "2022-01-01"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)

## json module for working with JSON data
### JSON serialization and deserialization
person = {"name": "John", "age": 30}
json_data = json.dumps(person)
print("JSON data:", json_data)

### Working with JSON data structures
json_string = '{"name": "John", "age": 30}'
parsed_json = json.loads(json_string)
print("Parsed JSON:", parsed_json)
