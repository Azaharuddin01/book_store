from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')