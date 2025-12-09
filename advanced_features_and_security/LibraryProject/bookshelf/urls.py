from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/add/', views.form_example, name='form_example'),
]
