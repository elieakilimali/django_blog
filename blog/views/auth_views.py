# views.py
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from ..forms import CustomUserCreationForm
from ..models import CustomUser

class SignUpView(CreateView):
    """Vue d'inscription des utilisateurs."""
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('login')  # Redirige vers la page de connexion après inscription

    def form_valid(self, form):
        """Enregistrer l'utilisateur et le connecter automatiquement."""
        user = form.save()  # Sauvegarde l'utilisateur dans la base de données
        login(self.request, user)  # Connecte l'utilisateur
        messages.success(self.request, 'Inscription réussie !')  # Message de succès
        return super().form_valid(form)


class CustomLoginView(LoginView):
    """Vue de connexion personnalisée."""
    template_name = 'blog/login.html'
    def get_success_url(self):
        """Retourne l'URL vers laquelle rediriger après la connexion."""
        # Par exemple, rediriger vers la page d'accueil après la connexion
        return reverse_lazy('home') 

class CustomLogoutView(LogoutView):
    """Vue de déconnexion personnalisée."""
    next_page = '/' 