from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from ..models.models import Post
# from ..forms import PostForm 

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at",]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(CreateView):
    model = Post
    # form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    # form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')