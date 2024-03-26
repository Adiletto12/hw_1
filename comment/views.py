from django.shortcuts import render, get_object_or_404
from comment.forms import CommentForm
from django.http import HttpResponse
from comment.models import Comment
from django.views import generic


class CommentList(generic.ListView):
    template_name = 'crud/comment_list.html'
    context_object_name = 'comment'
    model = Comment

    def get_queryset(self):
        return self.model.objects.all()


# def comment_list_view(request):
#     if request.method == 'GET':
#         comment = Comment.objects.all()
#         return render(request, template_name='crud/comment_list.html', context={'comment': comment})

class CommentDetail(generic.DetailView):
    template_name = 'crud/comment_detail.html'
    context_object_name = 'comment_id'
    model = Comment

    def get_object(self, **kwargs):
        comment_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=comment_id)


# def comment_detail_view(request, id):
#     if request.method == "GET":
#         comment_id = get_object_or_404(Comment, id=id)
#         return render(request, template_name='crud/comment_detail.html', context={
#             'comment_id': comment_id
#         })


class CommentDelete(generic.DeleteView):
    template_name = 'crud/comment_delete.html'
    success_url = '/comment_list/'
    model = Comment

    def get_object(self, **kwargs):
        comment_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=comment_id)


# def delete_comment_view(request, id):
#     comment_id = get_object_or_404(Comment, id=id)
#     comment_id.delete()
#     return HttpResponse('<h1>Comment Deleted Successfully</h1>')


class CommentCreate(generic.CreateView):
    template_name = 'crud/create_comment.html'
    form_class = CommentForm
    success_url = "/comment_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CommentCreate, self).form_valid(form=form)


# def create_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Comment create successfully!</h1>')
#     else:
#         form = CommentForm()
#     return render(request, template_name='crud/create_comment.html', context={'form': form})


# class CommentUpdate(generic.UpdateView):
#     template_name = 'crud/edit_comment.html'
#     form_class = CommentForm
#     success_url = '/comment_list/'
#     model = Comment


def edit_comment_view(request, id):
    comment_id = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Comment edit successfully!</h1>')
    else:
        form = CommentForm(instance=comment_id)
    return render(request, template_name='crud/edit_comment.html',
                  context={'form': form})


# class Search(generic.ListView):
#     template_name = 'crud/comment_list'
#     context_object_name = 'comment'
#     paginate_by = '5'
#
#     def get_queryset(self):
#         return Comment.objects.filter(name__icontains=self.request.GET.get('q'))
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#
