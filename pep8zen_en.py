"""
PEP8 Style Guide Examples
"""

# Introduction
"""
In the realm of code,
PEP8 serves as a wise guide,
Bringing clarity.

Readability reigns,
Consistency is the key,
Beauty in the code.
"""

# A Foolish Consistency is the Hobgoblin of Little Minds
"""
Consistency rules,
Guiding us through code's maze,
Hobgoblin, beware!

Be consistent, friend,
In style and in spirit,
Clarity shall bloom.
"""

# Code Layout

# Indentation
def my_function():
    """
    Indentation's dance,
    Graceful alignment of code,
    Harmony unfolds.
    """

def another_function():
    """
    Lines bow respectfully,
    With indents as their chorus,
    A symphony plays.
    """

# Tabs or Spaces?
def my_function():
    """
    Spaces, not tabs, rule,
    They align the code's rhythm,
    A visual delight.
    """

def another_function():
    """
    Spaces, soft whispers,
    Guiding eyes through code's passages,
    Order in chaos.
    """

# Maximum Line Length
very_long_variable_name = some_function(
    argument1, argument2, argument3, argument4
)

long_string = (
    "Lines stretching far,
    The code's narrative unfolds,
    Split for clarity.
    ")

# Blank Lines
def my_function():
    """
    Code takes a breath,
    Blank lines create pauses, peace,
    Balance in motion.
    """

def another_function():
    """
    Silence in between,
    Lines rest in the white spaces,
    A symphony's pause.
    """

# Source File Encoding
# No specific code example, only a mention of encoding, ensuring that the file speaks the same language as your code.

# Imports
import module1
import module2
import module3
import module4
import module5

# Whitespace

# Pet Peeves
# No specific code example, only mentions of avoiding extraneous whitespace and blank lines at the end of files.

# Other Recommendations
x = 5  # Spaces keep order,
        Between tokens, in control,
        Silence in the gaps.

y = some_function(argument1, argument2)

z = another_function(argument1, argument2)


# Comments

# Inline Comments
x = x + 1  # Increment x,
            A code annotation,
            Whispers of change.

y = y - 1  # Decrement y,
            A note to the reader,
            The story unfolds.

# Block Comments
"""
A tale untold yet,
Whispered secrets in plain sight,
Guiding the lost souls.
"""
x = 5
y = 10

"""
A story within,
Lines weave a tapestry, code,
Wisdom concealed.
"""
z = x + y

# Documentation Strings
def my_function():
    """
    Seekers of knowledge,
    Docstrings, your guiding light,
    Secrets now revealed.
    """

def another_function():
    """
    A script's enigma,
    Docstrings, your voice so clear,
    Clarity bestowed.
    """

# Naming Conventions

# Overriding Principle
# No specific code example, an eternal reminder to choose names that resonate with clarity and understanding.

# Descriptive: Naming Styles
# No specific code example, the journey towards meaningful and descriptive names begins within your heart.

# Prescriptive: Naming Conventions

## Names to Avoid
# No specific code example, whispers of caution, urging you to shun the forbidden names of obscurity and ambiguity.

## ASCII Compatibility
# No specific code example, reminding you to embrace the ancient tongue of ASCII for universal harmony.

## Package and Module Names
# No specific code example, guidance to use lowercase with underscores, forging paths that the codebase can traverse.

## Class Names
class MyClass:
    pass

class AnotherClass:
    pass

## Exception Names
try:
    # code that may raise an exception
except ValueError as e:
    # bravely capturing the exception, giving it a name that resonates with its identity

try:
    # code that may raise another exception
except KeyError as e:
    # fearlessly conquering yet another exception, armed with a name that reveals its essence

## Global Variable Names
GLOBAL_CONSTANT = 42

GLOBAL_VARIABLE = "Hello, world!"

## Function and Variable Names
my_variable = 42

another_variable = "Hello!"

def my_function():
    pass

def another_function():
    pass

# Function and Method Arguments

# Default Argument Values
def my_function(arg1, arg2=None):
    """
    Default paths unfold,
    Flexibility, your shield,
    Arguments embraced.
    """
    if arg2 is None:
        arg2 = []

def another_function(arg1, arg2=True, arg3=10):
    """
    A realm of options,
    Default values guide the way,
    Versatility.
    """
    pass

# Keyword Arguments and Positional Arguments
def my_function(arg1, arg2, *args, **kwargs):
    """
    Dance of arguments,
    Positional and keywords blend,
    Harmony in calling.
    """
    pass

def another_function(arg1, arg2, *args, **kwargs):
    """
    A symphony plays,
    The conductor, your function,
    Positional and keywords unite.
    """
    pass

# Function and Method Decorators
# No specific code example, the realm of decorators beckons, where functions and methods acquire new powers.

# Intermezzo: Coding Style
# No specific code example, a moment of respite, contemplating the grand tapestry of code style.

## Guidelines & Best Practices

### Use of the Backslash
my_string = (
    "Across lines it flows,
    The backslash binds as one,
    Code reads like verse.
    ")

another_string = (
    "Lines connected,
    The backslash creates a bridge,
    A story unfolds.
    ")

### When to Use Trailing Commas
my_list = [
    "item1",
    "item2",
    "item3",  # Trailing comma, a gentle touch,
                Readability in lists,
                Growth without pain.
]

another_list = [
    "item1",
    "item2",
    "item3",
]

### Accessing Protected Members
class MyClass:
    def __init__(self):
        self._protected_variable = 42

    def _protected_method(self):
        pass

class AnotherClass:
    def __init__(self):
        self._protected_variable = 10

    def _protected_method(self):
        pass

### Public and Internal Interfaces
class MyClass:
    def public_method(self):
        pass

    def _internal_method(self):
        pass

class AnotherClass:
    def public_method(self):
        pass

    def _internal_method(self):
        pass

# Conclusion
"""
Embrace PEP8's grace,
Code as a work of pure art,
Beauty in each line.
"""

# References
"""
Seek further wisdom,
Guidance from sages and more,
Code's journey goes on.
"""

