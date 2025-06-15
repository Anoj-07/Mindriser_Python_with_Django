# Type conversion 


# #TO INTEGER
# a ='234567'
# integer = int(a)
# print(integer + 1)

# a = 2.345
# integer = int(a) # give floor value
# print(integer) 

# #TO FLOAT
# a = '2'
# a = 20
# float_value = float(a)
# print(float_value / 2)

# #TO GROUP DATA(DATA STRUCTURE) => Except  for dictionary
# a = [1,2,3,4,5,6,3,4]
# b = set(a)
# c = tuple(a)
# d  = list(c)
# print(d)

# #TO DICTIONARY
# a = [['name', 'John'], ['age', 30], ['city', 'New York']]
# b = dict(a)
# print(b)

#TO STRING -> can be used to convert any data type to string


#TASK (Calculator)
#Ask the user for two numbers
#Ask the user for which operator to perform
#According to the operator user provides perform the operation with two numbers and print the value


first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = float(first_num) + float(second_num)
    print(result)
    
elif operator == '-':
    result = float(first_num) - float(second_num)
    print(result)
elif operator == '*':
    result = float(first_num) * float(second_num)
    print(result)
elif operator == "/":
    result = float(first_num) / float(second_num)
    print(result)
else:
    print("invalid operator")