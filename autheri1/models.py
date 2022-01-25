from django.db import models
import  uuid
# Create your models here.
class person_user(models.Model):
    ID=models.AutoField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    rollnumber=models.IntegerField()
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)

    
class room(models.Model):
    room_number=models.IntegerField()

