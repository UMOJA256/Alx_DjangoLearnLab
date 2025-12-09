from .models import Author, Book, Library, Librarian

# Query 1: All books by an author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# Query 2: All books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
