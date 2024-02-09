
from django.db import models

# Create your models here.
class RoomMember(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    