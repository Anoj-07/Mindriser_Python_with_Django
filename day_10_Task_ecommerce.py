import json

#-------------------------Main--------------------------------------
def main():
    user_input = input('Select the Type of user: 1. Buyer 2. Seller \n')
    if user_input == '1':
        buyer()
    elif user_input == '2':
        seller()
    else:
        print("Invalid input!")

#-------------------------Login & Register--------------------------
def login(user_type):
    user_choice = input("Enter a choice: 1. Register 2. Login \n")

    if user_choice == '1':
        while True:
            user_username = input("Enter your username: ")
            user_password = input("Enter your password: ")
            user_confirm_password = input("Confirm your password: ")

            if user_password == user_confirm_password:
                print("Registered successfully")

                user_dict_data = {
                    'username': user_username,
                    'password': user_password,
                    'type': user_type
                }

                user_json_data = json.dumps(user_dict_data)

                with open('users.txt', 'a') as f:
                    f.write(user_json_data + '-')
                break
            else:
                print('Passwords do not match. Try again.')

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
                    print("Login Successful !")
                    return user_dict_data['username'] # it check user name and it match give True other wise it give false
                    
            else:    
                print("Invalid username or password") 
                return None       
    else:
        print('Invalid input!')
        

#-------------------------Buyer--------------------------------------
def buyer():
    success = login('buyer')
    if success:
        while True:
            print("\nBuyer Options:")
            print("1. View all products")
            print("2. Purchase a product")
            print("3. View bills")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("Viewing all products...")
            elif choice == '2':
                print("Purchasing a product...")
            elif choice == '3':
                print("Viewing bills...")
            elif choice == '4':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")

#-------------------------Seller--------------------------------------
def seller():
    username = login('seller')
    if username:
        print(f"================Welcome {username}========================")
        while True:
            print("\nSeller Options:")
            print("1. View your products")
            print("2. Add a product")
            print("3. View bills")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                f = open('product.txt', 'r')
                product_data = f.read()
                f.close() 

                list_product_data = product_data.split('-')
                list_product_data.remove('')

                found = False
                for i in list_product_data:
                    product_dict_data = json.loads(i)
                    if product_dict_data.get('sellerName') == username:
                        print("***********Product Details:************")
                        print(f" Name    : {product_dict_data['productName']}")
                        print(f" Price   : {product_dict_data['price']}")
                        print(f" Quantity: {product_dict_data['quantity']}")
                        found = True
                if not found:
                        print(f"No product found")
                        


            # Adding Product
            elif choice == '2':
                product_name = input("Enter product name: \n")
                price = float(input("Enter price (In number) of your product: \n"))
                quantity = int(input("Enter Quantity (In number) of products: \n"))

                price('Add sucessfully')

                seller_dic = {
                    'productName': product_name,
                    'price': price,
                    'quantity': quantity,
                    'sellerName': username
                }

                user_json_data = json.dumps(seller_dic)

                with open('product.txt', 'a') as f:
                    f.write(user_json_data + '-')
                break
             

            elif choice == '3':
                print("Viewing bills...")
            elif choice == '4':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")

#-------------------------Run Program--------------------------------
main()
