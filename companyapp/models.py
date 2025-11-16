from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=500, default="")
    image = models.ImageField(upload_to='image_slider')
    
    def __str__(self):
        return self.title