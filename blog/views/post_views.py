from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Post
from ..forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    """Affiche la liste des articles publiés."""
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get_queryset(self):
        """Filtrer uniquement les articles publiés."""
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """Affiche les détails d'un article."""
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    """Création d'un article (réservé aux utilisateurs connectés)."""
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        """Associe automatiquement l'auteur connecté et gère l'image."""
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """Ajouter un contrôle pour l'auteur uniquement."""
        if not request.user.is_authenticated or not request.user.is_author:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Mise à jour d'un article (réservé à l'auteur uniquement)."""
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        """Vérifie si l'utilisateur est l'auteur de l'article."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Suppression d'un article (réservé à l'auteur uniquement)."""
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        """Vérifie si l'utilisateur est l'auteur de l'article."""
        post = self.get_object()
        return self.request.user == post.author
