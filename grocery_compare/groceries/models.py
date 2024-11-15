from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()  # API endpoint for the store
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability_date = models.DateTimeField()  # timestamp for price validity
    location = models.CharField(max_length=100)  # location for availability

    def __str__(self):
        return f"{self.product} - {self.store} - ${self.price}"

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_location = models.CharField(max_length=100)
    max_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    categories = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s Preferences"

from django.db import models

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
