import profile
from django.contrib import admin

# # Register your models here.
from autheri1.models import room
from autheri1.models import Profile

admin.site.register(room)
admin.site.register(Profile)