from django.db import models

# Create your models here.

class Photo(models.Model):
    img = models.ImageField(upload_to='static',default="")