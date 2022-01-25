from pickle import NONE
from django.db import models

# Create your models here.    
class room(models.Model):
    room_number=models.IntegerField()
    person_name=models.CharField(max_length=20,blank=True)
    status=models.BooleanField(default=False)
    def is_allocated(self):
        if room.status==0:
            return 0
        else:
            return 1

