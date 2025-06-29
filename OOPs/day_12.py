# OOP - programming way, object oriented programming
"""
This module demonstrates basic Object-Oriented Programming (OOP) concepts in Python.
Classes:
    Product:
        Represents a product with attributes: name, price, and quantity.
    Car:
        Represents a car with attributes: name, price, and max_speed.
        Methods:
            get_name(self): Prints the name of the car.
            set_name(self, name): Sets the name of the car and prints it.
Examples:
    - Creating instances of Product and Car.
    - Accessing and modifying object attributes.
    - Using methods to interact with object data.
"""

# Object - data + methods => form which every logic will be executes in our program
# Class - template (blue print) for creating objects
# data = object attributes


class Product:
    name = 'projector'
    price = 2300000
    quantity = 20


Product1 = Product()

# Product1.seller  = 'ram'
# pro = Product() 
# print(pro.seller)

print(Product1.name, Product1.price, Product1.quantity)

# ------------------------(methods) Inside class ----------------------------------------
class Car:
    name = 'volvo'
    price = '20M'
    max_speed = '300 km/hr'

    def get_name(self): # in self we can pass any name but self is a convention
        print(self.name)
    
    def set_name(self, name):
        self.name = name
        print(self.name)

    
car1 = Car()
car1.set_name('BMW')
car1.get_name()

# ---------------- Type of methods ------------------------

a = 'hello'.upper()
print(a)

class Car:
    name = 'volvo'
    price = '20M'
    max_speed = '300 km/hr'

car = Car()

# __perdefineName__ => magic method, it is used to get the name of the class
# print(car.__dir__())  # shows all the attributes and methods of the class

# __init__() - constructor 

class Car:
    name = 'volvo'
    price = '20M'
    max_speed = '300 km/hr'

    def __int__(self): # can be overridden
        print('This is a constructor')

car1 = Car()
car1.__int__()  # This will not work as __int__ is not a valid constructor name, it should be __init__

#Exmaple 2:
class Cars:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Car Name: {self.name}, Price: {self.price}'

car1 = Cars('BMW', '20M')
car2 = Cars('Audi', '30M')

print(car1.name)
print(car2.name, car2.price)
print(car1)