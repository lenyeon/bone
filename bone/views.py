from django.shortcuts import render
from .models import Post
def index(request):
    post_list = Post.objects.all()
    return render(request, 'bone/index.html', {'post_list':post_list})
def post_detail(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request, 'bone/post_detail.html', {'post':post})

# Create your views here.
