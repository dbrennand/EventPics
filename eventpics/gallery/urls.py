from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<uuid:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('gallery/upload_photos/', views.upload_photos, name='upload_photos'),
]
