from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/bicycle_images/', null=True, blank=True)
    special_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    special_price_valid_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class BikeComponents(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/bicycle_images/', null=True, blank=True)
    special_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    special_price_valid_until = models.DateField(null=True, blank=True)



