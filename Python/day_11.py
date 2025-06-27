#------------------------------------ Exception Handling----------------------------------------------------------------
# Try and Except are used to handle exceptions in Python.

# try:
#     num1 = int(input("Enter a number: "))
#     print(f"Your number is {num1}")
# except:
#     print("Invalid input! Please enter a valid number.")



try:
    num1 = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except NameError:
    print("Variable 'num' is not defined. Please check your code.")

