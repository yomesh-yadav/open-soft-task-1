from pickle import NONE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here. 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_allocated = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   

    
class room(models.Model):
    room_number=models.IntegerField()
    person_name=models.CharField(max_length=20,blank=True)
    status=models.BooleanField(default=False)
    

