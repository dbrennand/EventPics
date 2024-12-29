from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Gallery, Photo

@login_required
def index(request):
    galleries = Gallery.objects.filter(allowed_users=request.user)
    return render(request, 'gallery/index.html', {'galleries': galleries})

@login_required
def gallery_detail(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    # Ensure if the user doesn't have permission to the Gallery they cannot view it
    if request.user not in gallery.allowed_users.all():
        return redirect('index')
    # Get photos matching the gallery ID
    photos = Photo.objects.filter(gallery=gallery_id)
    return render(request, 'gallery/detail.html', {'photos': photos, 'gallery': gallery})

@login_required
def upload_photos(request):
    if request.method == 'POST':
        # Get the Gallery ID from the form
        gallery_id = request.POST.get('gallery')
        # Get the Gallery object from the database
        gallery = get_object_or_404(Gallery, id=gallery_id)
        # Get the photos from the form and create a Photo object in the database for each one
        photos = request.FILES.getlist('photos')
        for photo in photos:
            Photo.objects.create(gallery=gallery, photo=photo)
        return redirect('gallery_detail', gallery_id=gallery_id)
    return redirect('index')
