from django.urls import path
from . import views

urlpatterns = [
    path('relationships/', views.relationship_list, name='relationship-list'),
]

