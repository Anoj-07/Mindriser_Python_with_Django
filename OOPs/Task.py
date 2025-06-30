class Book:

    def __init__(self):
        book_name = input("Enter the book name: ")
        book_price = input("Enter the book price: ")
        book_descrription = input("Enter the book description: ")
        book_author = input("Enter the book author: ")

        self.name = book_name
        self.price = book_price
        self.description = book_descrription
        self.author = book_author
    
    def __str__(self):
        return f"Book name: {self.name}\nBook price: {self.price}\nBook description: {self.description}\nBook author: {self.author}"

class Library:

    library = []

    def add_book(self, book):
        self.library.append(book)
    
    def vi_all_books(self):
        for i, book in enumerate (self.library, start=1):
            print(f'{i}"." {book}')
    def search_book(self):
        search_book_name = input("Enter the book name you want to search: ")
        for i in self.library:
            if search_book_name == i.name:
                print(i)
            else:
                print("Book not found")
    def remove_book(self):
        self.vi_all_books()
        book_remove = input("Enter the book number you want to remove: ")
        try:
            self.library.pop(int(book_remove))
        except IndexError:
            print("Book not found")


library = Library()
while True:
    print("\n1. Add book")
    print("2. View all books")
    print("3. Search a book")
    print("4. Remove a book")
    print("5. Exit")
    user_choice = input("Enter your choice:  ")


    if user_choice == "1":
        book = Book()
        library.add_book(book)
        print("Book added successfully!")
    elif user_choice == "2":
        library.vi_all_books()
    elif user_choice == '3':
        library.search_book()
    elif user_choice == '4':
        library.remove_book()
    elif user_choice == '5':
        break


        
