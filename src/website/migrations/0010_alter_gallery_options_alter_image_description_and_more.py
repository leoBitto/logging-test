# Generated by Django 4.1.7 on 2023-09-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_rename_carousel_image_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, default='', help_text="identifica l'immagine", max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(blank=True, help_text='Non necessario se non deve essere inserita in una galleria', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.gallery'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_first',
            field=models.BooleanField(default=False, help_text='clicca se vuoi che sia la prima ad essere visualizzata in un eventuale galleria'),
        ),
    ]
