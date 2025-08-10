library_books = ["Python Basics", "Data Science 101", "Machine Learning", "AI for Beginners"]
while True:
    print("\nLibrary Menu:")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Available books:", library_books)
    elif choice == "2":
        book = input("Enter book name to borrow: ")
        if book in library_books:
            library_books.remove(book)
            print(f"Enjoy reading the book {book}")
        else:
            print("Book not available")
    elif choice == "3":
        book = input("Enter book name to return: ")
        library_books.append(book)
        print(f"Thank you for returning '{book}'.")
    elif choice == "4":
        print("Thank you for using the library system!")
        break
    else :
        print("Invalid choice!")