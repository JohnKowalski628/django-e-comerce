# Generated by Django 4.2.3 on 2023-09-05 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='#', null=True, upload_to='uploads/'),
        ),
    ]
