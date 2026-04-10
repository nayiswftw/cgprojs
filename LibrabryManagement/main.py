from add import add_book
from view import view_all_books
from search import search_book
from borrow import borrow_book
from return_book import return_book
from remove import remove_book

books = []
borrowed_books = []

while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Borrow")
    print("5. Return")
    print("6. Remove")
    print("7. Quit")
    print()
    
    choice = input("Pick: ")
    print()
    
    if choice == "1":
        add_book(books)
    elif choice == "2":
        view_all_books(books)
    elif choice == "3":
        search_book(books)
    elif choice == "4":
        borrow_book(books, borrowed_books)
    elif choice == "5":
        return_book(books, borrowed_books)
    elif choice == "6":
        remove_book(books)
    elif choice == "7":
        break
