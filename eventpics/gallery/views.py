from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery, Photo

def index(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery/index.html', {'galleries': galleries})

def gallery_detail(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    # Get photos matching the gallery ID
    photos = Photo.objects.filter(gallery=gallery_id)
    return render(request, 'gallery/detail.html', {'photos': photos, 'gallery': gallery})

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
