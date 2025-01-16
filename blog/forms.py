from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image', 'status']  # Utilise 'status' et non 'published'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-file'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3}),
        }




from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Formulaire d'inscription personnalisé
class CustomUserCreationForm(UserCreationForm):
  
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_image']

