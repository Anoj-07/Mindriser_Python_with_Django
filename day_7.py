#---------------------Day - 8---------------------------------

#-------------------------------- for loop --------------------------------------

# Iterable - Group data type(DS) -> EXample -> List

# Iterator - A variable which does iteration  -> Example -> i

# Iteration - Loop process of going from start to end of an iterable 

a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i ** 2)


# for i in a:
#     if i == 2:
#         continue # from here new loop will start
#     print(i)


for i in a:
    if i == 2:
        break # from here loop will break and end here
    # print(i)


#---------------------------------- FUNCTIONS (def)-------------------------------------------
# Make stattement reusable (Small piece of code that can be reusable)

# def Hello():
#     for i in range(0, 5):
#         print(i, 'Hello')

# Hello()

# -------Parameter and Arguments in functions----------
# def Hello_name(a, b):
#     print(a + b)

# Hello_name(20, 40)


a = 5
b = 6
def add(num1, num2):
    print(num1 + num2)

add(a, b)

c = 3
d = 8

add(c, d)
