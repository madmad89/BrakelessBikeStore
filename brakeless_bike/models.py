from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def subcategories(self):
        return Category.objects.filter(parent_category=self)

    def __str__(self):
        return self.name


class Product(models.Model):
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


class Cart(models.Model):
    STATUS = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='open')

    def __str__(self):
        return f'{self.status} cart of {self.user}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # @property
    # def get_total(self):
    #     total = self.product.price * self.quantity
    #     return total
    #
    # def __str__(self):
    #     return f'{self.quantity} X {self.product} in {self.cart}'
