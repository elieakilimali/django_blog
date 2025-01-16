from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post, Category, Comment

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_author')
    list_filter = ('is_staff', 'is_active', 'is_author')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'birthdate', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_author', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'bio', 'birthdate', 'profile_image'),
        }),
    )

# Enregistrer le CustomUserAdmin dans l'admin
admin.site.register(CustomUser, CustomUserAdmin)

# Enregistrer les autres modèles comme tu l'avais fait
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'content')
    list_filter = ('post', 'created_at')
    search_fields = ('content', 'user__username', 'post__title')
    ordering = ('-created_at',)

# Enregistrer les autres modèles
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
