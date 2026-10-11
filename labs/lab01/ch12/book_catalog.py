# Starting file for Lab 1 - Chapter 12 - book_catalog.py program
# James Kim, 10/10/2026, DEV128 Fall2026

# Defines code for listing book info in book catalog
def list_book(book_catalog):
    # Orders the books by title
    ordered_by_title = dict(sorted(book_catalog.items()))
    for title, book in ordered_by_title.items():
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}\n")

# Shows one book in book catalog
def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}")
    else:
        # Catches when book is not in book catalog
        print(f"Sorry, {title} doesn't exist in the catalog.")

# Edits book catalog
def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "add" and title in book_catalog:
        print(f"{title} already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(f"{title} doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    # Get remaining book data and create a dictionary for the data
    author = input("Author name: ")
    pubyear = input("Publication year: ")
    book = {title: {"author": author, "pubyear": pubyear}}

    # Add the book data to the catalog using the update operator
    book_catalog |= book

# Deletes book in book catalog
def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(f"{title} removed from catalog.")
    else:
        print(f"{title} doesn't exist in the catalog.")

def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("list - List All Books") # List command added
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    display_menu()
    book_catalog = {
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien", 
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    while True:
        print()
        command = input("Command: ").lower()
        # List command added
        if command == "list":
            list_book(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
