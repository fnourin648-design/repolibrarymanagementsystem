from django.contrib import admin
from django.urls import path
from .views import Viewbook, Addbook, Editbook, Deletebook
 

urlpatterns = [
    path('books/', Viewbook.as_view(), name='book_list'),
    path('books/add/', Addbook.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', views.Editbook.as_view(), name='edit_book'),
    path('books/<int:pk>/delete/', views.Deletebook.as_view(), name='delete_book'),
]