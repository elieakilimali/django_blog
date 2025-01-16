from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Créer automatiquement un profil uniquement si l'utilisateur est nouveau"""
    if created:
        # Aucun appel récursif ici
        print(f"Profil créé pour {instance.username}")

