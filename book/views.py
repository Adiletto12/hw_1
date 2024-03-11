from django.shortcuts import render
from book.models import Book

def books_view(request):
    if request.method == 'GET':
        query = Book.objects.all()
        return render(request, template_name='books.html',
                      context={'query': query})


