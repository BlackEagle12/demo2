from django.db import models

from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    priceOld = models.IntegerField()
    priceNew = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    ratting = models.IntegerField()
