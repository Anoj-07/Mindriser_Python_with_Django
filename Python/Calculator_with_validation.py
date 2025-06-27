#-------------------------TASK (Calculator)----------------------
#Ask the user for two numbers
#Ask the user for which operator to perform
#According to the operator user provides perform the operation with two numbers and print the value

while True:
#Check wheather the input is number or not before converting to int or float(Note: If user has provided number convert it to int or float if not then ask for number again)
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    

    check_1 = first_num.isdigit()
    check_2 = second_num.isdigit()

    if check_1 and check_2:
        num1 = float(first_num)
        num2 = float(second_num)
        break
    else:
        print("Number are only Allowed")

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