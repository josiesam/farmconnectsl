import uuid
from django.db import models
from django.core.exceptions import ValidationError
from marketinfo.models import MarketPrice

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    crop = models.ForeignKey(
            'marketinfo.Crop', on_delete=models.CASCADE, 
            editable=False, blank=True
            )
    environment = models.ForeignKey(
            'marketinfo.CropEnvironment',
            on_delete=models.CASCADE, 
            )
    market = models.ForeignKey(
            'marketinfo.MarketPrice', 
            editable=False,
            on_delete=models.CASCADE, 
            )
    image = models.ImageField( upload_to='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()
    advert = models.CharField(max_length=100, blank=True, null=True)
    seller = models.ForeignKey(
            'account.UserProfile', on_delete=models.CASCADE, 
            limit_choices_to={'is_farmer': True}
            )
    
    def __str__(self):
        return f'{self.crop}'

    def save(self, *args, **kwargs):
        self.crop = self.environment.crop


        market = MarketPrice.objects.filter(
                economic__crop=self.crop, 
                economic__environment=self.environment
            ).order_by('-date').first()
        if not market:
            raise ValidationError({'crop': 'No market price data for crop'})

        self.market = market

        return super().save(*args, **kwargs)



class Transaction(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE, related_name='buyer_transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
