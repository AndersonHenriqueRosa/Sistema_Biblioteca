# Generated by Django 4.2.7 on 2023-11-30 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_alter_books_cover_alter_books_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book-cover/'),
        ),
    ]