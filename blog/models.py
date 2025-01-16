from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from core.models import BaseModel
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Modèle CustomUser
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    is_author = models.BooleanField(default=False)


# Modèle Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Modèle Post
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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
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


# Modèle Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} a commenté {self.post.title}"
