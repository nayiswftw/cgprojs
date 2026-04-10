def view_all_books(books):
    if len(books) == 0:
        print("No books")
        print()
    else:
        for i in range(len(books)):
            book = books[i]
            status = book[2]
            if status == "available":
                print(str(i + 1) + ". " + book[0] + " - " + book[1] + " [AVAILABLE]")
            else:
                print(str(i + 1) + ". " + book[0] + " - " + book[1] + " [BORROWED by " + status + "]")
        print()
