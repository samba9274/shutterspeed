from django.contrib import admin
from .models import Photo
from .models import Profile

# Register your models here.

admin.site.register(Photo)
admin.site.register(Profile)