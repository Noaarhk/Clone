from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500,null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)