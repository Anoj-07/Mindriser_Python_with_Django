# Requirements
# Provide user login and register
# Provide user access to add balance, view balance and withdraw balance after login
# User's should be only able to work with their own balance data only

# Important - Use oop(Better program structure), File handling(Data storage), Git and Github for Version Control
import json
import os
class User:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
    
    def to_dic(self):
        return {
            "username": self.username,
            "password": self.password,
            "balance": self.balance
        }
    
    def from_dic(data):
        return User(data['username'], data['password'], data['balance'])


class UserStorage:
    def __init__(self, file = "User.txt"):
        self.file = file
        
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump([], f)
    
    def add_user(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        
        users = []
        for item in data:
            user = User.from_dic(item)
            users.append(user)
        return users
    
    def save_user(self, users):
        data = []
        for user in users:
            data.append(user.to_dic())
        
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)


class UserService:
    def __init__(self, storage):
        self.storage = storage

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        users = self.storage.add_user()

        for u in users:
            if u.username == username:
                print("Username already exists")
                return None
        
        new_user = User(username, password, 0.0)
        users.append(new_user)
        self.storage.save_user(users)
        print("User registered successfully")
        return new_user
    

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        users = self.storage.add_user()

        for u in users:
            if u.username == username and u.password == password:
                print("Login successful. ")
                return u
        print("Invalid username or password")
        return None
        
    def update_user(self, updated_user):
        users = self.storage.add_user()
        for i in range(len(users)):
            if users[i].username == updated_user.username:
                users[i] = updated_user
                break
        self.storage.save_user(users)


class WalletService:
    def __init__(self, user_service):
        self.user_service = user_service
    
    def view_balance(self, user):
        print(f"Your balance is {user.balance}")
    
    def add_balance(self, user):
        try:
            amount = float(input("Enter amount to add: Rs. "))
            if amount <= 0:
                print("Enter a valid amount! ")
                return
            
            user.balance += amount
            self.user_service.update_user(user)
            print(f"Rs. {amount:.2f} added to your account. ")
        
        except ValueError:
            print("Enter number only! ")
    
    def withdraw_balance(self, user):
        try:
            amount = float(input("Enter amount to withdraw: Rs."))
            if amount <= 0:
                print("Enter a valid amount! ")
                return
            if amount > user.balance:
                print("Insufficient balance! ")
                return
            
            user.balance -= amount
            self.user_service.update_user(user)
            print(f"Rs. {amount:.2f} withdrawn from your account. ")

        except ValueError:
            print("Enter number only! ")

def main():
    storage = UserStorage()
    user_service = UserService(storage)
    wallet_service = WalletService(user_service)
    current_user = None

    while True:
        if current_user is None:
            print("1. Register 2. Login 3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                current_user = user_service.register()
            elif choice == "2":
                current_user = user_service.login()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. ")
        
        else:
            print("1. View Balance 2. Add Balance 3. Withdraw Balance 4. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                wallet_service.view_balance(current_user)
            elif choice == '2':
                wallet_service.add_balance(current_user)
            elif choice == '3':
                wallet_service.withdraw_balance(current_user)
            elif choice == '4':
                current_user = None
                print("Logged out successfully. ")
            else:
                print("Invalid choice. ")
           
main()