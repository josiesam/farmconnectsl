from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files import File
from account.models import UserProfile
from faker import Faker
import random

fake = Faker()

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
    help = 'Generate dummy data for UserProfile model.'

    def handle(self, *args, **kwargs):
        self.generate_dummy_data()

    def generate_dummy_data(self):
        # Clear existing data (optional)
        UserProfile.objects.all().delete()

        # Generate dummy data
        for _ in range(20):  # Adjust the number of records as needed
            self.create_user_profile()

        self.stdout.write(self.style.SUCCESS('User data generation complete.'))

    def create_user_profile(self):
        user = User.objects.create(
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
        )
        profile = UserProfile.objects.get(user=user)

        profile.headshot=fake.image_url()
        profile.bio=fake.text()
        profile.address=fake.address()
        profile.is_farmer=random.choice([True, False])

        headshot_file = create_image_file('userprofile_headshot.jpg', 'image/jpeg')
        profile.headshot.save('userprofile_headshot.jpg', File(headshot_file))

        profile.save()
