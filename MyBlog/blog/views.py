from django.shortcuts import render
from .models import Post

# Create your views here.


def lists(request):
    data = {'Posts': Post.objects.all().order_by('date_post')}
    return render(request, 'blog/blog.html', data)


def posts(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})
