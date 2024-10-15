import random
from datetime import datetime, timedelta
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import UserProfile
from marketinfo.models import Crop, CropEnvironment, CropEconomic, MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle
from faker import Faker

fake = Faker()

# Helper function to create an image file
def create_image_file(filename, content_type):
    from django.core.files import File
    from PIL import Image
    from io import BytesIO
    from django.core.files.uploadedfile import InMemoryUploadedFile

    image = Image.new(
            mode='RGB', 
            size=(100, 100), 
            color=(
                random.randint(1,255),
                random.randint(1,255), 
                random.randint(1,255)
                )
            )
    image_io = BytesIO()
    image.save(image_io, format='PNG')
    image_file = InMemoryUploadedFile(
        image_io, None, filename, content_type, image_io.tell, None)
    image_file.seek(0)
    return image_file


class Command(BaseCommand):
    help = 'Generate dummy data for Crop-related models.'

    def handle(self, *args, **kwargs):
        self.generate_dummy_data()

    def generate_dummy_data(self):


        # Generate dummy data
        size = 6
        self.create_cropenvironment_data(size)


        self.stdout.write(self.style.SUCCESS('Dummy data generation complete.'))

    # Create Crop
 
    # Create CropEnvironment
    def create_cropenvironment_data(self, size):
        for _ in range(size):
            CropEnvironment.objects.create(
                crop=random.choice(Crop.objects.all()),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                altitude=fake.random_number(digits=2),
                soil_type=fake.word(),
                temperature_max=fake.random_number(digits=2),
                temperature_min=fake.random_number(digits=2),
                precipitation=fake.random_number(digits=2),
                humidity=fake.random_number(digits=2),
                wind_speed=fake.random_number(digits=2),
                soil_moisture=fake.random_number(digits=2),
                ph_level=fake.random_number(digits=2),
                nutrient_levels_nitrogen=fake.random_number(digits=2),
                nutrient_levels_phosphorus=fake.random_number(digits=2),
                remote_sensing_indices_ndvi=fake.random_number(digits=2),
                sensor_readings_light_intensity=fake.random_number(digits=2),
            )


  