import uuid
from django.db import models

class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Photo(models.Model):

    def upload_with_id(instance, filename):
        """
        Saves photos with the format <id>.<ext>
        <id> is the UUID of the photo assigned by Django.
        """
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        return filename

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_with_id)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
