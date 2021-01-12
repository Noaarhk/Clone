from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Photo(models.Model):
    user = models.ForeignKey(User, related_name='user_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
