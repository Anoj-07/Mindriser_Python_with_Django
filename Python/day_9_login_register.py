# Requirement 
# User should be able to register or login
# In register store user data
# In login ask user for his/her user info and check whether it exists or note
 # if exists login successfull
 # Else invalid credential

# -------------------------------------Module-----------------------------------------
 # convert dic to json and vice versa
import json 

user_choice = input("Enter a choice: 1. Register 2. Login \n")


if user_choice == '1':
    while True:
        user_username = input("Enter your username: ")
        user_password = input("Enter your password: ")
        user_confirm_password = input("Enter your confirm password: ")

        if user_password == user_confirm_password:
            print("Register successfully")
            
        
        # use dictionary for to store data if it have multiple data
            user_dict_data = {'username': user_username, 'password': user_password}

            user_json_data = json.dumps(user_dict_data)

            #Store the data
            f = open('users.txt', 'a')
            f.write(user_json_data + '-') # - it seprate data in txt file
            f.close()
            break
        else:
            print('Password do not match!')


elif user_choice == '2':
    user_username = input("Enter your userName: ")
    user_password = input("Enter your password: ")

    f = open('users.txt', 'r')
    user_data = f.read()
    f.close()

    list_user_data = user_data.split('-')
    list_user_data.remove('')

    
    for i in list_user_data:
        user_dict_data = json.loads(i)
        if user_dict_data.get('username') == user_username and user_dict_data.get('password') == user_password:
            print("Login Successful")
            break
    else:    
        print("Invalid username or password")            
    
else:
    print('Invald input!')