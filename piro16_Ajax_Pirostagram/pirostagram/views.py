from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    posts = Post.objects.all()
    form = CommentForm()
    return render(request, "home.html", {"posts":posts, "form":form})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
        return render(request, "create.html", {"form":form})

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_id = req["id"]
    action = req["action"]
    post = Post.objects.get(id=post_id)

    if action == "plus":
        post.like += 1
    else:
        post.like -= 1
    post.save()
    return JsonResponse({"id":post_id, "action":action})

@csrf_exempt
def comment(request):
    req = json.loads(request.body)
    post_id = req["id"]
    author = req["author"]
    content = req["content"]

    comment = Comment.objects.create(parent_post=get_object_or_404(Post, id=post_id), author=author, content=content)
    return JsonResponse({"id":post_id, "comment_id":getattr(comment, "id"), "author":author, "content":content})

@csrf_exempt
def delete(request):
    req = json.loads(request.body)
    comment_id = req["id"]
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({"id":comment_id})