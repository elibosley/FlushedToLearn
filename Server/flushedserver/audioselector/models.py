from django.db import models


# Create your models here.

class MusicFile(models.Model):
    media = models.FileField(upload_to='media/')
