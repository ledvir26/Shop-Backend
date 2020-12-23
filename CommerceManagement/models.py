from django.db import models

from products.models import Product 

# Create your models here.

class Management(models.Model):

    name = models.CharField(max_lemgth=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product = models.ForeignKey(, on_delete=models.CASCADE)
    create_in = models.models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
