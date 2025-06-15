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


# first_num = input("Enter first number: ")
# second_num = input("Enter second number: ")

# operator = input("Enter operator (+, -, *, /): ")

# if operator == '+':
#     result = float(first_num) + float(second_num)
#     print(result)
    
# elif operator == '-':
#     result = float(first_num) - float(second_num)
#     print(result)
# elif operator == '*':
#     result = float(first_num) * float(second_num)
#     print(result)
# elif operator == "/":
#     result = float(first_num) / float(second_num)
#     print(result)
# else:
#     print("invalid operator")



# -------------------LOOP STATEMENT(run multiple times)-----------------------------------------
# for loop (iterative loop) (run until the condition is false) (if you know the number of iterations)
a = 5
b = 0
for i in range(a):
    print("hello" + " ", i)

# while loop(conditional loop) (run until the condition is true) (if you don't know the number of iterations)
while a > b:
    # print('Hello world')
    b += 1

# Key_word in loops
# Break and continue

while True:
    print("Hello")
    print("Hello 2")
    break
    
count = 1
while  True:
    print("HI")
    if count == 5:
        break
    count +=1


# --- Try once ---
a = 5
b = 0
while a > b:
    b += 1
    if b == 2:
        continue
    print("HELLO")
    
