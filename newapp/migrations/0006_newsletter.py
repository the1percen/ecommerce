# Generated by Django 5.0.4 on 2024-06-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0005_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="newsletter",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
