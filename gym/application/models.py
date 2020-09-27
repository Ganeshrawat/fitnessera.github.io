from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class dataentry(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    itemlink=models.CharField(max_length=200)
    categ=models.CharField(max_length=100)

class item(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics',null= True)
    categ=models.CharField(max_length=100)
    details1= models.CharField(max_length=5000, default= "N/A")
    details2= models.CharField(max_length=5000, default= "N/A")
    details3= models.CharField(max_length=5000, default= "N/A")
