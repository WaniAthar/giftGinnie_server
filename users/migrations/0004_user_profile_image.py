# Generated by Django 5.1.4 on 2025-01-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_rename_first_name_user_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
