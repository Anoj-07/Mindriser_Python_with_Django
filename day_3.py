#conditional operator

# a = 23 
# b = 34

# : is called colon which is used to define a block of code after this is called block of code is called indentation
# if a > b :
#     print("A is greater")
# elif  a == b:
#     print("A is equal to B")
# else:
#     print("B is greater")

# #input statement 
# name = input("Enter you Name: ")
# print(name)

# print(name + "23")

# 
# Task =>
# Requirement 
# -> Make a list of valid usernames
# -> Ask for user's username
# -> If user's username is among valid username print Login successfull
# -> if not then print Invalid credentials
# 

valid_usernames = ["user1", "user2", "user3", "user4", "user5"]

user = input("Enter your username: ")

if user in valid_usernames:
    print("login successfull")
else:
    print("Invalid credentials")


