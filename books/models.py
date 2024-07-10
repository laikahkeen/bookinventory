from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
