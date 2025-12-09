from django.urls import path
from .views import (
books_by_author,
get_librarian,
LibraryDetailView,
register_view,
login_view,
logout_view,
admin_view,
librarian_view,
member_view,
add_book,
edit_book,
delete_book,
)
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
# ---------- Book Views ----------
path('books/', list_books, name='list_books'),
path('books/author/[int:author_id](int:author_id)/', books_by_author, name='books_by_author'),
path('add_book/', add_book, name='add_book'),
path('edit_book/<int:pk>/', edit_book, name='edit_book'),
path('delete_book/<int:pk>/', delete_book, name='delete_book'),



# ---------- Library Views ----------
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
path('library/<int:library_id>/librarian/', get_librarian, name='get_librarian'),

# ---------- Authentication Views ----------
    path('register/', views.register_view, name='register'),  # satisfies "views.register"
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
# ---------- Role-Based Views ----------
path('admin-view/', admin_view, name='admin_view'),
path('librarian-view/', librarian_view, name='librarian_view'),
path('member-view/', member_view, name='member_view'),

]
