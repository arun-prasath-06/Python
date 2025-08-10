'''Library Menu:
1. Display Books
2. Borrow Book
3. Return Book
4. Exit
Enter your choice: 1
Available books:
- Python Basics
- Data Science 101
- Machine Learning Guide

Enter your choice: 2
Enter book name to borrow: Python Basics
Book borrowed successfully!

Enter your choice: 1
Available books:
- Data Science 101
- Machine Learning Guide'''

books = ["Python Basics", "Data Science 101", "Machine Learning Guide"]
while True:
    print("\nLibrary Menu:")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice:")

    if choice == 1:
        print("Available Books:")
        for i in books:
            print("-",books)
    elif choice == 2:
        book = input("Enter Book name:")
        if book == books:
            books.remove(book)
            print("Book borrowed successfully!")
        else:
            print("Book not available!")
    elif choice == 3:
        book =input("Enter Book name:")
        if book not in books:
            books.append(book)
            print("Book returned successfully!")
        else:
            print("This book is already in the library!")
    elif choice == 4:
        print("Thank you for using the Library System!")
        break
    else :
        print("Invalid choice! Please select 1-4.")