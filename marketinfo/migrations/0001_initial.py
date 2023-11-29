# Generated by Django 4.2.7 on 2023-11-29 11:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('crop_type', models.CharField(help_text='The specific type of crop being cultivated (e.g., wheat, corn, soybeans).', max_length=255)),
                ('crop_variety', models.CharField(help_text='The specific variety or cultivar of the crop.', max_length=255)),
                ('planting_date', models.DateField(help_text='The date when the crop was planted.')),
                ('harvest_date', models.DateField(help_text='The date when the crop was harvested.')),
                ('plant_height', models.FloatField(blank=True, help_text='The height of the plants at a specific growth stage.', null=True)),
                ('leaf_area_index', models.FloatField(blank=True, help_text='The ratio of leaf area to ground area, indicating crop canopy density.', null=True)),
                ('biomass', models.FloatField(blank=True, help_text='The total weight of plant material per unit area.', null=True)),
                ('yield_amount', models.FloatField(help_text='The amount of crop produced per unit area.')),
                ('units', models.CharField(help_text='The unit of measurement for crop', max_length=100)),
                ('pest_incidence', models.CharField(help_text='Presence of pests and their severity.', max_length=255)),
                ('disease_incidence', models.CharField(blank=True, help_text='Presence of diseases and their severity.', max_length=255, null=True)),
                ('tillage_practices', models.CharField(blank=True, help_text='Information about plowing and cultivation.', max_length=255, null=True)),
                ('irrigation_practices', models.CharField(blank=True, help_text='Frequency and amount of irrigation.', max_length=255, null=True)),
                ('crop_rotation', models.CharField(blank=True, help_text='Information about the rotation of crops in the field.', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CropEconomic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('cost_of_inputs', models.FloatField(help_text='The cost of seeds, fertilizers, pesticides, etc.')),
                ('revenue', models.FloatField(help_text='Income generated from the sale of the crop.')),
                ('profit_loss', models.FloatField(help_text='Calculated based on revenue and input costs.')),
                ('quality_parameters_moisture_content', models.FloatField(help_text='Moisture content of the harvested crop.')),
                ('quality_parameters_grain_size', models.CharField(help_text='Grain size of the harvested crop.', max_length=255)),
                ('crop', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='marketinfo.crop')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('registration_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubmittedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MarketPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('economic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketinfo.cropeconomic')),
            ],
        ),
        migrations.CreateModel(
            name='CropEnvironment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('latitude', models.FloatField(help_text='Geographic coordinates of the crop field.')),
                ('longitude', models.FloatField(help_text='Geographic coordinates of the crop field.')),
                ('altitude', models.FloatField(blank=True, help_text='Elevation of the crop field.', null=True)),
                ('soil_type', models.CharField(blank=True, help_text='Information about the soil composition.', max_length=255, null=True)),
                ('temperature_max', models.FloatField(blank=True, help_text='Daily maximum temperature.', null=True)),
                ('temperature_min', models.FloatField(blank=True, help_text='Daily minimum temperature.', null=True)),
                ('precipitation', models.FloatField(blank=True, help_text='Amount of rainfall or irrigation.', null=True)),
                ('humidity', models.FloatField(blank=True, help_text='Relative humidity levels.', null=True)),
                ('wind_speed', models.FloatField(help_text='Speed of the wind.')),
                ('soil_moisture', models.FloatField(blank=True, help_text='Moisture content in the soil.', null=True)),
                ('ph_level', models.FloatField(blank=True, help_text='Acidity or alkalinity of the soil.', null=True)),
                ('nutrient_levels_nitrogen', models.FloatField(blank=True, help_text='Concentration of nitrogen in the soil.', null=True)),
                ('nutrient_levels_phosphorus', models.FloatField(blank=True, help_text='Concentration of phosphorus in the soil.', null=True)),
                ('remote_sensing_indices_ndvi', models.FloatField(blank=True, help_text='Normalized Difference Vegetation Index (NDVI) from remote sensing data.', null=True)),
                ('sensor_readings_light_intensity', models.FloatField(blank=True, help_text='Light intensity from sensors measuring various environmental factors.', null=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketinfo.crop')),
            ],
        ),
        migrations.AddField(
            model_name='cropeconomic',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketinfo.cropenvironment'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketinfo.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_registered', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketinfo.event')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
    ]
