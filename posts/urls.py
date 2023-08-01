from django.urls import path, include
from .views import *

urlpatterns = [
    path("list/", PostsListPageView.as_view(), name="posts_list"),
    path("post/", PostCreatePageView.as_view(), name="post_create"),
    path("<pk>/", PostDetailPageView.as_view(), name="post_detail"),
]
