from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, You're the Admin")

def home(request):
    return HttpResponse("You're in Home page now...")

def post(request, post_id):
    return HttpResponse(f"You're viewing the post with post ID of {post_id}")