from django.urls import path
from .views import *

urlpatterns = [
    path("books/", view_books, name="books"),
    path("books/add/", view_add_book, name="add_book"),
    path("books/remove/<int:id>/", view_remove_book, name="remove_book"),
    path("books/update/<int:id>/", view_update_book, name="update_book"),
    
    path("authors/", view_authors, name="authors"),
    path("authors/add/", view_add_author, name="add_author"),
    path("authors/remove/<int:id>/", view_remove_author, name="remove_author"),
    path("authors/update/<int:id>/", view_update_author, name="update_author")
]
