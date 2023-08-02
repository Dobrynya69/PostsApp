from django.urls import path, include
from .views import *

urlpatterns = [
    path("list/", PostsListPageView.as_view(), name="posts_list"),
    path("list/<pk>/", UserPostsListPageView.as_view(), name="user_posts_list"),
    path("post/", PostCreatePageView.as_view(), name="post_create"),
    path("post/<user_pk>/<post_pk>/", PostChangePageView.as_view(), name="post_change"),
    path("<pk>/", PostDetailPageView.as_view(), name="post_detail"),
]
