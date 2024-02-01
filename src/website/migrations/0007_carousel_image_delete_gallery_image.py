# Generated by Django 4.1.7 on 2023-09-29 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_gallery_image_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_first', models.BooleanField(default=False)),
                ('carousel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.carousel')),
            ],
        ),
        migrations.DeleteModel(
            name='Gallery_image',
        ),
    ]
