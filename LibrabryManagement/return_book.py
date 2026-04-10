def return_book(books, borrowed_books):
    if len(books) == 0:
        print("No books")
        print()
    else:
        name = input("Return: ")
        print()
        
        found = False
        for i in range(len(books)):
            if books[i][0].lower() == name.lower():
                found = True
                if books[i][2] != "available":
                    books[i][2] = "available"
                    for j in range(len(borrowed_books)):
                        if borrowed_books[j][0].lower() == name.lower():
                            borrowed_books.pop(j)
                            break
                    print("Returned!")
                    print()
                else:
                    print("Already available")
                    print()
                break
        
        if found == False:
            print("Not found")
            print()
