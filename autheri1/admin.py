from django.contrib import admin

# # Register your models here.
from autheri1.models import person_user,room

admin.site.register(person_user)
admin.site.register(room)