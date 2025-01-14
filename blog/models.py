from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from core.models import BaseModel

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    is_author = models.BooleanField(default=False)



# Modèle de Catégorie
class Category(models.Model):
    """Modèle de catégorie pour classer les articles."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Modèle de Post
class Post(BaseModel):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = [
        (DRAFT, 'Brouillon'),
        (PUBLISHED, 'Publié'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def is_published(self):
        return self.status == self.PUBLISHED


# Modèle de Commentaire
class Comment(models.Model):
    """Modèle de commentaire associé à un article."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} a commenté {self.post.title}"


# # Modèle de Profil Utilisateur (facultatif si CustomUser est utilisé)
class Profile(models.Model):
    """Profil utilisateur supplémentaire."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"
