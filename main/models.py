from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="main/")
    
    def __str__(self):
        return self.name
    