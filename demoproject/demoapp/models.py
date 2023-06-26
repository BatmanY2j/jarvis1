from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    nm=models.CharField(max_length=15)
    im=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self):
        return self.nm
