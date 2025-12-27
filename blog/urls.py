from django.urls import path 
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>", views.detail, name="detail"),
    path("old_url", views.old_url_view, name="old_url"),
    path("new_test_url", views.new_url_view, name="new_post_url")
]