# Defining Functions

#Functions syntax and parameters
#Return values

# Functions in python are defined using the 'def' keyword, followed by the function name
# parentheses (), inside the parentheses you put a parameter name, and the colon.


# Example 1:
def multiply(a, b):
    return a * b
result = multiply(8, 15)
print(result)

# Example 2: Multiple return values

def get_coordinates():
    return 30, 40

x, y = get_coordinates()
print(x, y)

# Exercise 1: Define a function greet with a parameter name, set to 'John', and print a message
# I am a software programmer

def greet(name='John'):
    print(f"I am a software programmer, {name}")

greet()

# Example 3: Return multiple values 
def get_name_and_position():
    name = 'Alice Brown'
    position = 'I am a data scientist'
    return name, position
name, position = get_name_and_position()
print(name, position)

# Exercise 4: Return multiple return values of your name and age

def get_name_and_age():
    name = 'Emily Wilson'
    age = 32
    return name, age
name, age = get_name_and_age()
print(name, age)

# Notes

"""_summary_
def: keyword to define a function
function_name: name of the function
parameters: Optional, arguments passed to the function
Docstrings: Optional, describes the function purpose
return: optional, returns a value from the function
    """
# Syntax for defining a function
#def function_name(parameters):
#   """_summary_"""
#    function body
#    return value
 
#Lambda function
# Lambda functions a small anonymous functions defined using the lambda keyword
# They are restricted to a single expression

# Syntax for lambda function
#lymbda parameter: expression

# Example 4: Create a lambda function to add two numbers

add = lambda a, b: a + b
print(add(75, 90))

# Example 5: Use cases of lambda function for sorting

coordinates = [(6, 3), (7, 1), (4, 2), (5, 0)]

coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map, Filter and Reduce
# Example 6: Get the squares of 6 to 10 using map, filter and reduce

number_squares = [6, 7, 8, 9, 10]

squares = list(map(lambda x: x**2, number_squares))

print(squares)

# Exercise 4: Define a function to get user info that accepts arbitrary keyword arguments and prints each key value pair

get_user_info = lambda **kwargs: [print(f"{key}: {value}") for key, value in kwargs.items()]
get_user_info(name="Alice", age=32, occupation="Data Analyst")