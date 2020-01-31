from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    image_url = models.URLField()
    long_description = models.CharField(max_length=500)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} with name: {self.name}"
