def search_book(books):
    word = input("Find: ")
    print()
    
    for book in books:
        if word.lower() in book[0].lower():
            status = book[2]
            if status == "available":
                print(book[0] + " - " + book[1] + " [AVAILABLE]")
            else:
                print(book[0] + " - " + book[1] + " [BORROWED by " + status + "]")
    
    print()
