# Generated by Django 3.1.2 on 2020-10-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_image_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='jpeg',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='png',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
