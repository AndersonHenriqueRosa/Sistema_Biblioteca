# Generated by Django 4.2.7 on 2023-11-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_literary_genres_genres_alter_books_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Genre'},
        ),
        migrations.RenameField(
            model_name='books',
            old_name='number_book',
            new_name='quantity_book',
        ),
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]