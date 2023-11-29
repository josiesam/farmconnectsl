import random
from django.core.management.base import BaseCommand
from faker import Faker
from marketinfo.models import Crop, CropEnvironment, CropEconomic, MarketPrice
from account.models import UserProfile
from marketplace.models import Product, Transaction

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for Product and Transaction models.'

    def add_arguments(self, parser):
        parser.add_argument('--size', type=int, help='Number of records to generate')

    def handle(self, *args, **kwargs):
        size = kwargs['size'] if kwargs['size'] else 10
        self.generate_dummy_data(size)

    def generate_dummy_data(self, size):
        # Clear existing data (optional)
        Product.objects.all().delete()
        Transaction.objects.all().delete()

        # Generate dummy data
        self.create_product_data(size)
        self.create_transaction_data(size)


    def create_product_data(self, size):
        for _ in range(size):
            environment = random.choice(CropEnvironment.objects.all()) 

            seller = random.choice(UserProfile.objects.filter(is_farmer=True))
            if MarketPrice.objects.filter( economic__crop=environment.crop, economic__environment=environment).exists():
                product = Product.objects.create(
                    environment=environment,
                    price=fake.random_number(digits=2),
                    available_quantity=fake.random_number(digits=2),
                    seller=seller,
                )
        self.stdout.write( self.style.SUCCESS(f'Product data generation complete. Generated {size} records.'))

    def create_transaction_data(self, size):

        for _ in range(size):
            transaction = Transaction.objects.create(
                buyer=random.choice(UserProfile.objects.all()),
                product=random.choice(Product.objects.all()),
                quantity=fake.random_number(digits=2),
                total_price=fake.random_number(digits=3),
                transaction_date=fake.date_this_month(),
            )

        self.stdout.write( self.style.SUCCESS(f'Transaction data generation complete. Generated {size} records.'))
