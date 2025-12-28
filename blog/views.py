from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post
# Create your views here.

# posts = [
#         {"id":1, "title": "Post 1", "content": "Post Content 1"},
#         {"id":2, "title": "Post 2", "content": "Post Content 2"},
#         {"id":3, "title": "Post 3", "content": "Post Content 3"},
#         {"id":4, "title": "Post 4", "content": "Post Content 4"},
#     ]

def index(request):
    posts = Post.objects.all()
    blog_title = "New Posts"
    return render(request, 'index.html', {'blog_title': blog_title, "posts": posts})

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

        # post = next((item for item in posts if item.id == post_id), None)
        print(post)
        logger = logging.getLogger("TESTING")
        logger.debug(f"Post Data is {post}")
    except Post.DoesNotExist as e:
        raise Http404("Post Does Not Exist...")
    return render(request, 'detail.html', {'post': post})

def post(request, post_id):
    return HttpResponse(f"You're viewing the post with post ID of {post_id}")

def old_url_view(request):
    return redirect(reverse("blog:new_post_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")