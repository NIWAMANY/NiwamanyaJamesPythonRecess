# Inheritance and Polymorphism

"""
Summary:
- Inheritance and method overriding
- Polymorphism and method resolution order
- Abstract classes and interfaces
"""

# Inheritance and Method Overriding

"""
Description:
Inheritance allows a child class to inherit attributes and methods from a parent class.
Method overriding allows a child class to provide a specific implementation of a method
that is already defined in its parent class.
"""

# Example 1: Create a class where a Dog inherits from Animal and overrides the speak method

class Animal:
    def speak(self):
        return 'Generic Animal Sound'

class Dog(Animal):
    def speak(self):
        return 'Barks'

# Implementation of inherited classes
animal = Animal()
dog = Dog()

print(animal.speak())  # Output: Generic Animal Sound
print(dog.speak())     # Output: Barks

# Polymorphism and Method Resolution Order (MRO)

"""
Polymorphism allows objects of different classes to be treated as objects of a common superclass.
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
"""

# Example 2: How polymorphism works in Python

class Cat(Animal):
    def speak(self):
        return 'Meow'

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  # Output: Barks
make_animal_speak(Cat())  # Output: Meow

# Exercise 1: Create a simple application to manage different types of vehicles

"""
Requirements:
1. Base class: Vehicle
   Attributes: make, model, year
   Methods: display_info()

2. Derived classes:
   Car: Inherits from Vehicle
   Attributes: number_of_doors
   Overrides: display_info()

   Motorcycle: Inherits from Vehicle
   Attributes: type_of_bike (cruiser, sport, touring)
   Overrides: display_info()
"""

# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Derived class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")

# Derived class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_of_bike}")

# Exercise 2: Polymorphism
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # Empty line for readability

# Create instances of vehicles
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Softail", 2019, "Cruiser")

# Create a list of vehicles
vehicles = [car, motorcycle]

# Call the display_vehicle_info function
display_vehicle_info(vehicles)

# Reading and Writing Files in Python

"""
Summary:
- Working with text files
- Handling CSV files
- JSON and XML file processing
"""

# Reading and Writing Text Files

"""
Key Concepts:
- Opening a file: open() function (modes: r, w, a, r+)
- Reading a file: read() function
- Writing to a file: write() function
- Closing a file: close() function
"""

# Example 3: Write to a file and read from a file

# Writing to a text file
with open('example.txt', 'w') as file:
    file.write('I am learning Python and I love it.\n')
    file.write('I use Python for automation.')

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Handling CSV Files

"""
CSV (Comma Separated Values) is a common file format used to store tabular data, such as spreadsheets or tables.
Python provides a module called csv to handle CSV files.
"""

# Example 4: Writing and Reading CSV files

import csv

# Writing to a CSV file
with open('example.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Position', 'Course'])
    writer.writerow(['John Doe', 'Student', 'Computer Science'])

# Reading from a CSV file
with open('example.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML File Processing

"""
JSON (JavaScript Object Notation) and XML (eXtensible Markup Language) are formats used to structure data.
"""

# Example 5: Writing and Reading JSON files

import json

# Writing to a JSON file
student_data = {
    'name': 'John Doe',
    'course': 'Computer Science',
    'year': 'Year 2'
}
with open('student.json', 'w') as json_file:
    json.dump(student_data, json_file)

# Reading from a JSON file
with open('student.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)

# Writing and Reading XML files

import xml.etree.ElementTree as ET

# Creating the root element
root = ET.Element("students")

# Creating some student elements
student1 = ET.SubElement(root, "student", id="s101")
ET.SubElement(student1, "name").text = "John Doe"
ET.SubElement(student1, "major").text = "Computer Science"
ET.SubElement(student1, "gpa").text = "3.5"

student2 = ET.SubElement(root, "student", id="s102")
ET.SubElement(student2, "name").text = "Jane Smith"
ET.SubElement(student2, "major").text = "Engineering"
ET.SubElement(student2, "gpa").text = "3.8"

# Creating a tree and writing to a file
tree = ET.ElementTree(root)
tree.write("students.xml")

print("Student data XML file written successfully!")

# Parsing the XML file
tree = ET.parse("students.xml")
root = tree.getroot()

print("Student data XML file read successfully!")

# Iterating over the students
for student in root:
    print("Student ID:", student.get("id"))
    print("Name:", student.find("name").text)
    print("Major:", student.find("major").text)
    print("GPA:", student.find("gpa").text)
    print("---")

# Exercise 3: Using abstraction to calculate the area and perimeter of a rectangle

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create a rectangle object
rect = Rectangle(5, 3)

# Calculate and print the area and perimeter
print("Area:", rect.area())            # Output: Area: 15
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 16
