from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import AuthorForm, BookForm


###   books  ###

def view_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "books.html", {"books": books})


def view_add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books")
    else:
        form = BookForm()

    return render(request, "add_book.html", {"form": form})


def view_update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books")
    else:
        form = BookForm(instance=book)

    return render(request, "update_book.html", {"form": form})


def view_remove_book(request, id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=id)
        book.delete()
        return redirect("books")


###   authors  ###
    
def view_authors(request):
    authors = Author.objects.prefetch_related("books").all()
    return render(request, "authors.html", {"authors": authors})


def view_add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authors")
    else:
        form = AuthorForm()

    return render(request, "add_author.html", {"form": form})


def view_update_author(request, id):
    author = get_object_or_404(Author, id=id)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("authors")
    else:
        form = AuthorForm(instance=author)

    return render(request, "update_author.html", {"form": form})


def view_remove_author(request, id):
    if request.method == "POST":
        author = get_object_or_404(Author, id=id)
        author.delete()
        return redirect("authors")