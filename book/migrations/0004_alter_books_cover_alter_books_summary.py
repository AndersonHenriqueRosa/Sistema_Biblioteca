# Generated by Django 4.2.7 on 2023-11-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_genres_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='books',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
