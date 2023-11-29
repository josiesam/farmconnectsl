import uuid

from django.db import models
from django.utils.text import slugify


from django.db import models

# Agronomic Model


class Crop(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    crop_type = models.CharField(
        max_length=255, help_text="The specific type of crop being cultivated (e.g., wheat, corn, soybeans).")
    crop_variety = models.CharField(
        max_length=255, help_text="The specific variety or cultivar of the crop.")
    planting_date = models.DateField(
        help_text="The date when the crop was planted.")
    harvest_date = models.DateField(
        help_text="The date when the crop was harvested.")
    plant_height = models.FloatField(
        help_text="The height of the plants at a specific growth stage.", blank=True, null=True)
    leaf_area_index = models.FloatField(
        help_text="The ratio of leaf area to ground area, indicating crop canopy density.", blank=True, null=True)
    biomass = models.FloatField(
        help_text="The total weight of plant material per unit area.", blank=True, null=True)
    yield_amount = models.FloatField(
        help_text="The amount of crop produced per unit area.")
    units = models.CharField(help_text="The unit of measurement for crop", max_length=100)
    pest_incidence = models.CharField(
        max_length=255, help_text="Presence of pests and their severity.", blank=True, null=True)
    disease_incidence = models.CharField(
        max_length=255, help_text="Presence of diseases and their severity.", blank=True, null=True)
    tillage_practices = models.CharField(
        max_length=255, help_text="Information about plowing and cultivation.", blank=True, null=True)
    irrigation_practices = models.CharField(
        max_length=255, help_text="Frequency and amount of irrigation.", blank=True, null=True)
    crop_rotation = models.CharField(
        max_length=255, help_text="Information about the rotation of crops in the field.", blank=True, null=True)

    def __str__(self):
        return f"{self.crop_type}: {self.crop_variety}"

# Environmental Model


class CropEnvironment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    crop = models.ForeignKey('Crop', on_delete=models.CASCADE)
    latitude = models.FloatField(
        help_text="Geographic coordinates of the crop field.",
        )
    longitude = models.FloatField(
        help_text="Geographic coordinates of the crop field.",
        )
    altitude = models.FloatField(
            help_text="Elevation of the crop field.",
            blank=True, null=True
            )
    soil_type = models.CharField(
        max_length=255, help_text="Information about the soil composition.",
        blank=True, null=True
        )
    temperature_max = models.FloatField(
            blank=True, null=True,
            help_text="Daily maximum temperature.")
    temperature_min = models.FloatField(
            blank=True, null=True,
            help_text="Daily minimum temperature.")
    precipitation = models.FloatField(
            blank=True, null=True,
        help_text="Amount of rainfall or irrigation.")
    humidity = models.FloatField(
            blank=True, null=True,
            help_text="Relative humidity levels.")
    wind_speed = models.FloatField(help_text="Speed of the wind.")
    soil_moisture = models.FloatField(
            blank=True, null=True,
        help_text="Moisture content in the soil.")
    ph_level = models.FloatField(
            blank=True, null=True,
        help_text="Acidity or alkalinity of the soil.")
    nutrient_levels_nitrogen = models.FloatField(
            blank=True, null=True,
        help_text="Concentration of nitrogen in the soil.")
    nutrient_levels_phosphorus = models.FloatField(
            help_text="Concentration of phosphorus in the soil.",
            blank=True, null=True,
            )
    remote_sensing_indices_ndvi = models.FloatField(
        help_text="Normalized Difference Vegetation Index (NDVI) from remote sensing data.", 
        blank=True, null=True,
        ) 
    sensor_readings_light_intensity = models.FloatField(
        blank=True, null=True,
        help_text="Light intensity from sensors measuring various environmental factors.", 
        )
    class Meta:
        unique_together = ('crop', 'longitude', 'latitude', )

    def __str__(self):
        return f'{self.crop} ({self.longitude}, {self.latitude})'

# Economic Model


class CropEconomic(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    crop = models.ForeignKey(
        'Crop', on_delete=models.CASCADE, blank=True)
    environment = models.ForeignKey(
        'CropEnvironment', on_delete=models.CASCADE)
    cost_of_inputs = models.FloatField(
        help_text="The cost of seeds, fertilizers, pesticides, etc.")
    revenue = models.FloatField(
        help_text="Income generated from the sale of the crop.")
    profit_loss = models.FloatField(
        editable=False,
        help_text="Calculated based on revenue and input costs.")
    quality_parameters_moisture_content = models.FloatField(
        help_text="Moisture content of the harvested crop.")
    quality_parameters_grain_size = models.CharField(
        max_length=255, help_text="Grain size of the harvested crop.")

    def save(self, *args, **kwargs):
        self.crop = self.environment.crop
        self.profit_loss = self.cost_of_inputs - self.revenue
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.environment} - {self.crop}'


class MarketPrice(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    economic = models.ForeignKey('CropEconomic', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.economic.crop} price {self.date}'


class Event(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    registration_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Update the slug field based on the title field
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Attendee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        'account.UserProfile', on_delete=models.CASCADE)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.event}: User({user_profile.user})'


class BlogPost(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the slug field based on the title field
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title})'


class Comment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}: User({user.user})'


class UserSubmittedArticle(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Update the slug field based on the title field
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}: User({user.author.user})'
