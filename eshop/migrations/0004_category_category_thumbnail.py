# Generated by Django 4.2.3 on 2023-09-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_categoryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_thumbnail',
            field=models.ImageField(blank=True, default='#', null=True, upload_to='uploads/'),
        ),
    ]