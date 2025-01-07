from django.urls import path
from .views.post_views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from .views.comment_views import CommentCreateView
from .views.base import HomePageView

urlpatterns = [
    path("",HomePageView.as_view(), name="home"),
    path("post",PostListView.as_view(), name="post_list"),
    path ("post/<slug:slug>/",PostDetailView.as_view(), name="post_detail"),
    path("post/new/",PostCreateView.as_view(),name="post_create"),
    path("post/<slug:slug>/edit/",PostUpdateView.as_view(), name="post_edit"),
    path("post/<slug:slug>/delete/",PostDeleteView.as_view(), name="post_delete")

]


# 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