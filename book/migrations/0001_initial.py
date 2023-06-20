# Generated by Django 4.2.2 on 2023-06-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("book_name", models.CharField(max_length=100)),
                ("author_name", models.CharField(max_length=100)),
                ("publisher_name", models.CharField(max_length=100)),
                ("Description", models.TextField(blank=True)),
                ("language", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("book_type", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("available_for", models.CharField(blank=True, max_length=100)),
                ("book_image", models.ImageField(blank=True, upload_to="")),
            ],
        ),
    ]