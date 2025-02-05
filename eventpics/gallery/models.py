import uuid
from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):
    """
    Gallery model.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    allowed_users = models.ManyToManyField(
        User, related_name="allowed_galleries", blank=True
    )

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    """
    Photo model.
    """

    def upload_with_id(instance, filename):
        """
        Saves a photo with the format <id>.<ext>
        <id> is the UUID of the photo assigned by Django.
        """
        ext = filename.split(".")[-1]
        filename = f"{instance.id}.{ext}"
        return filename

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_with_id)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
