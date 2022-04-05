import profile
from django.contrib import admin

# # Register your models here.
from project_app.models import room
from project_app.models import Profile

admin.site.register(room)
admin.site.register(Profile)