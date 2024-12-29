from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Photo

@receiver(post_delete, sender=Photo)
def delete_photo_from_s3(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(save=False)
