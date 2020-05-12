from django.shortcuts import render
from .models import Photo
from .models import Profile

# Create your views here.

def index(request):
    context = {
        'profile': Profile.objects.filter(id=1).first(),
        'title': "Photographer",
    }
    return render(request, 'gallery/index.html', context)

def gallery(request):
    context = {
        'profile': Profile.objects.filter(id=1).first(),
        'photos': Photo.objects.all(),
        'title': "Gallery",
    }
    return render(request, 'gallery/gallery.html', context)

def photo_view(request, photo_id=1) :
    context = {
        'profile': Profile.objects.filter(id=1).first(),
        'title': "Photo",
        'photo': Photo.objects.filter(id=photo_id).first(),
    }
    return render(request, 'gallery/photo_view.html', context)