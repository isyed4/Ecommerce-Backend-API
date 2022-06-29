from django.db import models

class Electronics(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)


