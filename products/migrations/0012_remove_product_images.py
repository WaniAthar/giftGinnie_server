# Generated by Django 5.1.4 on 2025-01-14 08:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_product_created_at_product_updated_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="images",
        ),
    ]
