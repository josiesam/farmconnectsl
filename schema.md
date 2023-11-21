# FarmConnect Schema

## Account app

```py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    headshot = models.ImageField(upload_to='userprofile/headshot', blank=True, null=True)

    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

# Additional Fields can be added as needed, such as contact information, farm details, etc.

```

## MarketInfo app

```py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

# You can add more fields like optimal growing conditions, etc.

class MarketPrice(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

```

## Marketplace app
```py
from django.db import models
from account.models import UserProfile

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='products')

# Additional Fields can be added as needed, such as product images, certification details, etc.

class Transaction(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='buyer_transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

```