from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.FloatField()
