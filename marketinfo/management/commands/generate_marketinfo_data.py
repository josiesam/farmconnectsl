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
        # Clear existing data (optional)
        Crop.objects.all().delete()
        CropEnvironment.objects.all().delete()
        CropEconomic.objects.all().delete()
        MarketPrice.objects.all().delete()
        Event.objects.all().delete()
        Attendee.objects.all().delete()
        BlogPost.objects.all().delete()
        Comment.objects.all().delete()
        UserSubmittedArticle.objects.all().delete()

        # Generate dummy data
        size = 10
        self.create_crop_data(size)
        self.create_cropenvironment_data(size)
        self.create_cropeconomic_data(size)
        self.create_marketprice_data(size)
        self.create_event_data(size)
        self.create_attendee_data(size)
        self.create_blogpost_data(size)
        self.create_comment_data(size)
        self.create_userarticle_data(size)

        self.stdout.write(self.style.SUCCESS('Dummy data generation complete.'))

    # Create Crop
    def create_crop_data(self, size):
        for _ in range(size):
             Crop.objects.create(
                crop_type=fake.word(),
                crop_variety=fake.word(),
                planting_date=fake.date_this_decade(),
                harvest_date=fake.date_this_year(),
                plant_height=fake.random_number(digits=2),
                leaf_area_index=fake.random_number(digits=2),
                biomass=fake.random_number(digits=2),
                yield_amount=fake.random_number(digits=2),
                units=fake.word(),
                pest_incidence=fake.word(),
                disease_incidence=fake.word(),
                tillage_practices=fake.word(),
                irrigation_practices=fake.word(),
                crop_rotation=fake.word(),
            )

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

        # Create CropEconomic
    def create_cropeconomic_data(self, size):
        for _ in range(size):
            environment=random.choice(CropEnvironment.objects.all())
            CropEconomic.objects.create(
                environment=environment,
                crop=environment.crop,
                cost_of_inputs=fake.random_number(digits=2),
                revenue=fake.random_number(digits=2),
                profit_loss=fake.random_number(digits=2),
                quality_parameters_moisture_content=fake.random_number(digits=2),
                quality_parameters_grain_size=fake.word(),
            )

        # Create MarketPrice
    def create_marketprice_data(self, size):
        # Create Crop
        for _ in range(size):
            MarketPrice.objects.create(
                economic=random.choice(CropEconomic.objects.all()),
                price=fake.random_number(digits=2),
                date=fake.date_this_decade(),
            )

        # Create Event
    def create_event_data(self, size):
        for _ in range(size):
            event = Event.objects.create(
                title=fake.word(),
                description=fake.text(),
                location=fake.word(),
                date=fake.date_this_decade(),
                time=fake.time(),
                registration_link=fake.url(),
            )

        # Create Attendee
    def create_attendee_data(self, size):
        # Create Crop
        for _ in range(size):
            Attendee.objects.create(
                event=random.choice(Event.objects.all()),
                user_profile=random.choice(UserProfile.objects.all()),
                is_registered=fake.boolean(),
            )

        # Create BlogPost
    def create_blogpost_data(self, size):
        for _ in range(size):
            blog_post = BlogPost.objects.create(
                title=fake.word(),
                content=fake.text(),
                author=random.choice(UserProfile.objects.all()),
                publication_date=fake.date_this_decade(),
            )
            image_file = create_image_file('blogpost_image.jpg', 'image/jpeg')
            blog_post.image.save('blogpost_image.jpg', File(image_file))

        # Create Comment
    def create_comment_data(self, size):
        for _ in range(size):
            Comment.objects.create(
                post=random.choice(BlogPost.objects.all()),
                user=random.choice(UserProfile.objects.all()),
                text=fake.text(),
                date=fake.date_this_decade(),
            )

        # Create UserSubmittedArticle
    def create_userarticle_data(self, size):
        for _ in range(size):
            UserSubmittedArticle.objects.create(
                title=fake.word(),
                content=fake.text(),
                author=random.choice(UserProfile.objects.all()),
                submission_date=fake.date_this_decade(),
                is_approved=fake.boolean(),
            )
