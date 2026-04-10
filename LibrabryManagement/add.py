def add_book(books):
    name = input("Book: ")
    author = input("Author: ")
    print()
    
    book = [name, author, "available"]
    books.append(book)
    print("Added!")
    print()
