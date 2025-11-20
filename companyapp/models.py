from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='image_slider')
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=200, db_default='')
    image1 = models.ImageField(upload_to='image1_about', null=True, blank=True)
    description = models.TextField(max_length=600, default='')
    short_description1 = models.TextField(max_length=600, db_default='')
    title_headline1 = models.CharField(max_length=100, db_default='')
    title_healine2 = models.CharField(max_length=100, db_default='')
    title_headline3 = models.CharField(max_length=100, db_default='')
    short_description2 = models.TextField(max_length=600, db_default='')
    image2 = models.ImageField(upload_to='image2_about', null=True, blank=True)
    video = models.CharField(max_length=100, db_default='')
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    icon_service = models.CharField(max_length=100, db_default='')
    title = models.CharField(max_length=100, db_default='')
    description = models.TextField(max_length=300, db_default='')
    speed = models.TextField(max_length=100, default='')
    
    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    category = models.CharField(max_length=100, db_default='')
    title = models.CharField(max_length=200, db_default='')
    short_description = models.TextField(max_length=500, default='')
    client = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=1000, db_default='')
    image = models.ImageField(upload_to='image_portfolio')
    
    def __str__(self):
        return self.title