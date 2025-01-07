from django.contrib import admin
from .models.models import Post, Category, Comment, Profile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'published', 'author', 'category')
    list_filter = ('published', 'created_at', 'category')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    prepopulated_fields = {'slug': ('title',)} 
    ordering = ('-created_at',)
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = "Marquer comme publié"

    def make_unpublished(self, request, queryset):
        queryset.update(published=False)
    make_unpublished.short_description = "Marquer comme non publié"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'content')
    list_filter = ('post', 'created_at')
    search_fields = ('content', 'user__username', 'post__title')
    ordering = ('-created_at',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birthdate', 'image')
    search_fields = ('user__username', 'bio')
    ordering = ('user__username',)

# Enregistrer les modèles dans l'admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
