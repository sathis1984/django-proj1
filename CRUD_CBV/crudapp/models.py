from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=100)
    auth_name=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.IntegerField()

    def get_absolute_url(self):
        return reverse ('list')
       #  return reverse('details',kwargs={'pk':self.pk})
