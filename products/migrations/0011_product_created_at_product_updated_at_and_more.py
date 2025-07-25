# Generated by Django 5.1.4 on 2025-01-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0010_remove_productcategory_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default="2025-01-14 13:47:19.741322"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="productimage",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default="2025-01-14 13:47:19.74132"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productimage",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
