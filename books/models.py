from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length =255)
    content = models.TextField(max_length =2048)


