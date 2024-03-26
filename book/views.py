from django.shortcuts import render, get_object_or_404
from book.models import Book
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'books.html'
    context_object_name = 'query'
    model = Book

    def get_queryset(self):
        return self.model.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'books_detail.html'
    context_object_name = 'query_id'
    model = Book

    def get_object(self, **kwargs):
        query_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=query_id)

# def books_detail_view(request, id):
#     if request.method == 'GET':
#         query_id = get_object_or_404(Book, id=id)
#         return render(request, template_name='books_detail.html', context={'query_id': query_id})


class SearchView(generic.ListView):
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex