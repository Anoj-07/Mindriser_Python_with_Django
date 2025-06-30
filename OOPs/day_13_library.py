# Library (OOP)

# Requirements
# Give user choices: 1. Add book 2. View all books 3. Remove a book 4. Search a book
    # 1. Add books - ask user for name,price,description,author and store it in list
    # 2. View all books - print all the books stored in list
    # 3. Remove a book - ask for book name which he/she wants to remove then remove it from the list
    # 4. Search a book - ask for the book name to search then print the book if exists else print not found
    
class Book:
    def __init__(self, title, author, price, description):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
    
    def __str__(self):
        return f"{self.title} by {self.author} - Rs.{self.price}\nDescription: {self.description}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def view_books(self):
        return self._books
    
    def remove_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return True
        return False
    
    def search_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None
    

def user_input():

    title = input("Title: ")
    author = input("Author: ")

    while True:
        price_input = input("Price: ")
        try:
            price = float(price_input)
            break
        except ValueError:
            print("Please enter a valid number ")
        
    description = input("Description: ")
    return title, author, price, description


def main():
    lib = Library() # it is like creating an object of Library class

    while True:
        print("\n1. Add book")
        print("2. View all books")
        print("3. Remove a book")
        print("4. Search a book")
        print("5. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            title, author, price, description = user_input()
            book = Book(title, author, price, description)
            lib.add_book(book)
            print("Book added successfully!")
        
        elif user_choice == '2':
            all_books = lib.view_books()
            if all_books:
                for book in all_books:
                    print(book)
            else:
                print("No books in the library.")
        
        elif user_choice == '3':
            title = input("Enter the title of the book you want to remove: ")
            removed = lib.remove_book(title)
            if removed:
                print("Book removed successfully!")
            else:
                print("Book not found in the library.")
        
        elif user_choice ==  '4':
            title = input("Enter the name of the book you want to search: ")
            book = lib.search_book(title)
            if book:
                print("Your book",book)
            else:
                print("Book not found in the library.")
        elif user_choice == '5':
            print("Exit.....")
            break

        else:
            print("Invalid choice. Please try again.")

main()