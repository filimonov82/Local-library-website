from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language


def index(request):
    num_books = Book.objects.count()
    word_books = Book.objects.filter(title__icontains='не').count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'word_books': word_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres
    }

    return render(request, 'index.html', context=context)
