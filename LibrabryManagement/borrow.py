def borrow_book(books, borrowed_books):
    if len(books) == 0:
        print("No books")
        print()
    else:
        name = input("Borrow: ")
        person = input("Your name: ")
        print()
        
        found = False
        for i in range(len(books)):
            if books[i][0].lower() == name.lower():
                found = True
                if books[i][2] == "available":
                    books[i][2] = person
                    borrowed_books.append([books[i][0], books[i][1], person])
                    print("Got it!")
                    print()
                else:
                    print("Already borrowed by " + books[i][2])
                    print()
                break
        
        if found == False:
            print("Not found")
            print()
