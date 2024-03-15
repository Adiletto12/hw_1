from django.shortcuts import render, get_object_or_404
from book.models import Book

def books_view(request):
    if request.method == 'GET':
        query = Book.objects.all()
        return render(request, template_name='books.html',
                      context={'query': query})


def books_detail_view(request, id):
    if request.method == 'GET':
        query_id = get_object_or_404(Book, id=id)
        return render(request, template_name='books_detail.html', context={'query_id': query_id})