# Generated by Django 4.2.16 on 2024-10-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_author_author_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="book_covers/"),
        ),
    ]
