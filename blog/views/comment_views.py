from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Comment, Post
from ..forms import CommentForm


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        """Personnalisation de la validation du formulaire."""
        post = get_object_or_404(Post, pk=self.kwargs['pk'])  # Récupérer le post lié
        form.instance.user = self.request.user
        form.instance.post = post  # Associer le commentaire au post
        messages.success(self.request, "Votre commentaire a été ajouté avec succès !")
        return super().form_valid(form)

    def get_success_url(self):
        """Redirige vers le détail de l'article après soumission."""
        return self.object.post.get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        """Vérifie que l'utilisateur est authentifié avant de permettre l'ajout d'un commentaire."""
        if not request.user.is_authenticated:
            messages.error(self.request, "Vous devez être connecté pour commenter.")
            return redirect('login')  # Redirige l'utilisateur vers la page de connexion
        return super().dispatch(request, *args, **kwargs)
