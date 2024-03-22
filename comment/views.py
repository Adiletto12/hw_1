from django.shortcuts import render, get_object_or_404
from comment.forms import CommentForm
from django.http import HttpResponse

from comment.models import Comment


# Create your views here.

def comment_list_view(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        return render(request, template_name='crud/comment_list.html', context={'comment': comment})

def comment_detail_view(request, id):
    if request.method == "GET":
        comment_id = get_object_or_404(Comment, id=id)
        return render(request, template_name='crud/comment_detail.html', context={
            'comment_id': comment_id
        })

def delete_comment_view(request, id):
    comment_id = get_object_or_404(Comment, id=id)
    comment_id.delete()
    return HttpResponse('<h1>Comment Deleted Successfully</h1>')


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Comment create successfully!</h1>')
    else:
        form = CommentForm()
    return render(request, template_name='crud/create_comment.html', context={'form': form})


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
