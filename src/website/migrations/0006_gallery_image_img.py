# Generated by Django 4.1.7 on 2023-09-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_gallery_image_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
