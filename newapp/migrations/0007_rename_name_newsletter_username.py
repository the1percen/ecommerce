# Generated by Django 5.0.4 on 2024-06-02 15:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0006_newsletter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsletter",
            old_name="name",
            new_name="username",
        ),
    ]
