from django.core.management.base import BaseCommand
from account.models import UserProfile
from django.core.files import File
from core.models import ContactUs, Team, Affiliation, FAQ
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
    help = 'Generate dummy data for ContactUs, Team, Affiliation, and FAQ models.'

    def handle(self, *args, **kwargs):
        self.generate_dummy_data()

    def generate_dummy_data(self):
        # Clear existing data (optional)
        ContactUs.objects.all().delete()
        Affiliation.objects.all().delete()
        FAQ.objects.all().delete()

        # Generate dummy data
        for _ in range(10):  # Adjust the number of records as needed
            self.create_contact_us()
            self.create_affiliation()
            self.create_faq()

        self.stdout.write(self.style.SUCCESS('Dummy data generation complete.'))

    def create_contact_us(self):

        ContactUs.objects.create(
            user=random.choice(UserProfile.objects.all()),
            subject=fake.word(),
            message=fake.text(),
        )

    def create_team(self):
        team = Team.objects.create(
            name=fake.name(),
            profile=fake.image_url(),
            bio=fake.text(),
            organization=fake.company(),
            role=fake.job(),
        )
        profile_file = create_image_file('team_profile.jpg', 'image/jpeg')
        team.profile.save('team_profile.jpg', File(profile_file))

    def create_affiliation(self):
        affiliation = Affiliation.objects.create(
            name=fake.company(),
            bio=fake.text(),
            logo=fake.image_url(),
        )
        logo_file = create_image_file('team_logo.jpg', 'image/jpeg')
        affiliation.logo.save('team_logo.jpg', File(logo_file))

    def create_faq(self):
        FAQ.objects.create(
            topic=fake.word(),
            question=fake.sentence(),
            answer=fake.paragraph(),
        )
