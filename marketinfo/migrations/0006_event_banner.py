# Generated by Django 4.2.7 on 2023-12-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketinfo', '0005_crop_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='banner',
            field=models.ImageField(default='', upload_to='event/banner'),
            preserve_default=False,
        ),
    ]
