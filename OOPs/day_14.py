# python built in classes

# Enumerate

a = ['hello', 'world', 'python']

b = list(enumerate(a))
print(b)


# lambda function
# lambda arguments: expression
# => lambda a, b: a + b => It is a function that takes two arguments and returns their output.
# def add(a, b):
#     return a + b

add = lambda a, b : a + b
print(add(2, 3))

# map class
# map(function, iterable)
# map(function, iterable1, iterable2, iterable3, ..., iterableN)
# It applies the function to each element of the iterable and returns a map object.

a = [1, 2, 3, 4, 5]

def multiply(a):
    return a * 2

print(list(map(multiply, a)))

# Ternary Operator (short hand if else)

a = 2 
b = 3

c = "a is greater than b" if a > b else "b is greater than a"
print(c)
print("a is greater than b") if a > b else print("b is greater than a")

# Decorators

def hello(func):
    print('hello')
    func()
    print('byee')

@hello
def greet():
    print('hello world')