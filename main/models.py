# Create your models here.
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='albums/', default='none.jpeg')
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()