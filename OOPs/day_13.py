# OOPs concepts
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction
#=========================================================================

# 1. Inheritance 

# can be re-use the code 

class Vehicle: # parents class
     wheels = 4

     def get_wheels(self):
          print(self.wheels)

class Car(Vehicle): # Child class
     pass

car1 = Car()
car1.get_wheels()

class Vehicle: # parents class
     wheels = 4

     def get_wheels(self):
          print(self.wheels)

class Example:
     name = 'hello'

class Car(Vehicle, Example): # Child class
     pass

car1 = Car()
car1.get_wheels()
print(car1.name)


# 2. Abbstraction
# => hiding the implementation details 
#  use module abc

from abc import abstractmethod, ABC

class Animal(ABC):
 
    @abstractmethod # first it run the abstract method
    def move(self): # then it run
        print("hello")

class Human(Animal):
     # same method name as abstract class
     def move(self):
          print('I can walk and run')

h = Human()
h.move()


# 3. polymorphism
# => same method name but different functionality

class Animal:
    def move(self):
          print("It is walking")
    
class Bird:
    def move(self):
          print("It is flying")

a = Animal()
b = Bird()
a.move()
b.move()

# 4. Encapsulation
# => binding the data and function together

class User:
    def __init__(self, name, password, email):
         self.name = name # public variable
         self.__password = password # private variable
         self._email = email # protected variable
    
    def _get_name(self): # protected method
         print(self.name)
    
    def __get_pass(self): # private method
        print(self.__password)


user1 = User()
print(user1.username)


# Library (OOP)

# Requirements
# Give user choices: 1. Add book 2. View all books 3. Remove a book 4. Search a book
    # 1. Add books - ask user for name,price,description,author and store it in list
    # 2. View all books - print all the books stored in list
    # 3. Remove a book - ask for book name which he/she wants to remove then remove it from the list
    # 4. Search a book - ask for the book name to search then print the book if exists else print not found