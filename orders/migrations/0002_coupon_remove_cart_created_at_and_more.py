# Generated by Django 5.1.4 on 2025-01-15 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0015_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
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
                ("code", models.CharField(max_length=50, unique=True)),
                (
                    "discount_type",
                    models.CharField(
                        choices=[("PERCENT", "PERCENT"), ("FLAT", "FLAT")],
                        max_length=10,
                    ),
                ),
                (
                    "discount_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("valid_from", models.DateTimeField()),
                ("valid_until", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Coupon",
                "verbose_name_plural": "Coupons",
            },
        ),
        migrations.RemoveField(
            model_name="cart",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="delivery_address",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="status",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="updated_at",
        ),
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cart Item",
                "verbose_name_plural": "Cart Items",
            },
        ),
        migrations.AddField(
            model_name="cart",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cart",
                to="orders.coupon",
            ),
        ),
    ]
