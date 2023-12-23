# Generated by Django 4.2.2 on 2023-07-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='lon_discription',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about_media/'),
        ),
    ]
