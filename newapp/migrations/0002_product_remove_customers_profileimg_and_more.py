# Generated by Django 5.0.4 on 2024-06-01 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("price", models.FloatField()),
                ("digital", models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="customers",
            name="profileimg",
        ),
        migrations.RemoveField(
            model_name="customers",
            name="username",
        ),
        migrations.AddField(
            model_name="customers",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="customers",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="customers",
            name="email",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="Order",
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
                ("date_orderd", models.DateTimeField(auto_now_add=True)),
                ("complete", models.BooleanField(default=False, null=True)),
                ("transaction_id", models.CharField(max_length=200, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="newapp.customers",
                    ),
                ),
            ],
        ),
    ]