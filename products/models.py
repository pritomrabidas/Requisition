from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name