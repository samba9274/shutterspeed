from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="gallery-index"),
    path('gallery', views.gallery, name="gallery-gallery"),
    path('photo/<int:photo_id>/', views.photo_view, name="gallery-photo"),
]
