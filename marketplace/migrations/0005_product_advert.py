# Generated by Django 4.2.7 on 2023-12-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_transaction_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='advert',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
