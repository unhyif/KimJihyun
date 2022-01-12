from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # Queryset
    return render(request, 'blog/post_list.html', {'posts': posts}) # model에서 필요한 정보를 받아 template에 전달, 오른쪽 posts는 parameter

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
