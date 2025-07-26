'''
# hello.py
print("Hello, Python!")

# keywords_list.py
import keyword
print(keyword.kwlist)

# variables_operators.py
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# data_types.py
x = 10              # int
y = 5.5             # float
z = "Hello"         # str
flag = True         # bool
print(type(x), type(y), type(z), type(flag))

# numeric_sequence_boolean.py
num = 100             # numeric
name = "Alice"        # sequence
is_valid = True       # boolean
print(num, name, is_valid)

# Control Structures and Conditional Statements
# 07_if_statement.py
x = 10
if x > 5:
    print("x is greater than 5")

# 08_if_else.py
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
# 09_if_elif_else.py
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
  
# 10_for_loop.py
for i in range(1, 6):
    print("Number:", i)
   
# 11_while_loop.py
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 12_nested_loop.py
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
 
# 13_break_continue_pass.py
for i in range(5):
    if i == 2:
        continue  # Skips printing 2
    if i == 4:
        break     # Stops at 4
    print("i:", i)

def sample():
    pass  # Placeholder for future code

# 14_input_output.py
name = input("Enter your name: ")
print("Hello,", name)


#Lists, Dictionaries, and Sets
# list_intro.py
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
 
# list_methods_slicing.py
numbers = [10, 20, 30, 40, 50]

# Methods
numbers.append(60)
numbers.remove(20)
numbers.insert(2, 25)

# Slicing
print("List:", numbers)
print("First 3 elements:", numbers[:3])
print("Last 2 elements:", numbers[-2:])

# dict_intro.py
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}
print("Name:", student["name"])
print("Age:", student.get("age"))

# dict_methods.py
student = {"name": "Bob", "marks": 90}
student["course"] = "Math"
student.update({"grade": "A"})
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# set_intro.py
colors = {"red", "green", "blue", "red"}
print("Unique Colors:", colors)

# set_methods.py
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

set1.add(6)
set1.discard(2)
print("Updated Set1:", set1)

#Python Functions & Lambda Expressions
# function_basic.py
def greet():
    print("Hello from a function!")
greet()
# function_with_params.py
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)
# default_args.py
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Pooja")
# keyword_args.py
def student(name, age):
    print(f"Name: {name}, Age: {age}")
student(age=22, name="John")
# arbitrary_args.py
def total(*numbers):
    print("Sum:", sum(numbers))
total(10, 20, 30)
# lambda_function.py
square = lambda x: x * x
print("Square of 4:", square(4))
add = lambda a, b: a + b
print("Add:", add(3, 5))

#String, Number, and DateTime Functions
# string_functions.py
text = "  Hello Python  "
print("Original:", text)
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())
print("Replace:", text.replace("Python", "World"))
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Split:", text.strip().split(" "))
# number_functions.py
x = -5
y = 4.75
print("Absolute:", abs(x))
print("Round:", round(y))
print("Power:", pow(2, 3))  # 2^3 = 8
print("Max:", max(10, 20, 30))
print("Min:", min(10, 20, 30))
# datetime_functions.py
import datetime
# Current date and time
now = datetime.datetime.now()
print("Now:", now)
# Current date only
today = datetime.date.today()
print("Today:", today)
# Custom date
dob = datetime.date(2000, 5, 25)
print("DOB:", dob)
# Formatting date
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

# class_object.py
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Alice")
s1.display()


# access_specifiers.py
class Demo:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    # def show(self):
    #     print(self.public)
    #     print(self._protected)
    #     print(self.__private)

obj = Demo()
# obj.show()

print(obj.public)        # Accessible
print(obj._protected)    # Accessible (but use with caution)
# print(obj.__private)   # Error: Name mangling
# print(obj._Demo__private)  # Accessing private via name mangling


# constructor.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("John", 30)
p1.display()

# inheritance.py
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# polymorphism.py
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly.")

class Parrot(Bird):
    def flight(self):
        print("Parrots can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

b = Bird()
p = Parrot()
o = Ostrich()

b.flight()
p.flight()
o.flight()

# method_overriding.py
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

c = Child()
c.show()


#File Handling in Python (Text & Binary Files)
# text_file_handling.py

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, this is a sample file.\n")
    f.write("Python file handling is easy!\n")

# Reading the file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# binary_file_handling.py

data = {"name": "Alice", "marks": 85}

import pickle

# Write binary data
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Read binary data
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
    print("Binary Loaded Data:", loaded)

# try_except_else.py
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("No errors occurred.")

# try_finally.py
try:
    print("Inside try block")
    x = 10 / 0
finally:
    print("Finally block always executes.")

# exception_args.py
try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)

# raise_exception.py
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("You cannot divide by zero!")
    return x / y

print(divide(10, 2))
print(divide(10, 0))  # Uncomment to see the exception
'''
# user_defined_exception.py
class AgeTooSmallError(Exception):
    pass
age = 15
if age < 18:
    raise AgeTooSmallError("Age is too small to vote")
