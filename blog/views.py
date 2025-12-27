from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title = "New Posts"
    posts = [
        {"id":1, "title": "Post 1", "content": "Post Content 1"},
        {"id":2, "title": "Post 2", "content": "Post Content 2"},
        {"id":3, "title": "Post 3", "content": "Post Content 3"},
        {"id":4, "title": "Post 4", "content": "Post Content 4"},
    ]
    return render(request, 'index.html', {'blog_title': blog_title, "posts": posts})

def detail(request, post_id):
    return render(request, 'detail.html')

def post(request, post_id):
    return HttpResponse(f"You're viewing the post with post ID of {post_id}")

def old_url_view(request):
    return redirect(reverse("blog:new_post_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")