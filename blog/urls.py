from django.urls import path
from .views.post_views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from .views.comment_views import CommentCreateView
from .views.base import HomePageView

from .views.auth_views import SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Page d'accueil
    path('', HomePageView.as_view(), name='home'),

    # Articles
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Commentaires
    # path('posts/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),


    ####################################
    path('signup/', SignUpView.as_view(), name='signup'),  # Page d'inscription
    path('login/', CustomLoginView.as_view(), name='login'),  # Page de connexion
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
