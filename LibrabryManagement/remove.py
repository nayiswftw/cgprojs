def remove_book(books):
    if len(books) == 0:
        print("No books")
        print()
    else:
        name = input("Remove: ")
        print()
        
        found = False
        for i in range(len(books)):
            if books[i][0].lower() == name.lower():
                books.pop(i)
                print("✓")
                print()
                found = True
                break
        
        if found == False:
            print("Not found")
            print()
    return books
