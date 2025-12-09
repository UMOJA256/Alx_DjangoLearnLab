from .models import Author, Book, Library, Librarian

# -------------------------------
# Query all books by a specific author
# -------------------------------
def books_by_author(author_name):
    """
    Returns all books written by the given author name.
    """
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# -------------------------------
# List all books in a specific library
# -------------------------------
def books_in_library(library_name):
    """
    Returns all books available in the specified library.
    """
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# -------------------------------
# Retrieve the librarian for a library
# -------------------------------
def librarian_for_library(library_name):
    """
    Returns the librarian assigned to the given library.
    """
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# -------------------------------
# Example usage (for testing)
# -------------------------------
if __name__ == "__main__":
    # Replace with actual names from your database
    print("Books by Author 'J.K. Rowling':")
    for book in books_by_author("J.K. Rowling"):
        print(f"- {book.title}")

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library("Central Library"):
        print(f"- {book.title}")

    print("\nLibrarian for 'Central Library':")
    librarian = librarian_for_library("Central Library")
    print(f"- {librarian.name}")
