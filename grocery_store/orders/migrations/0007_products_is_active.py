# Generated by Django 5.1.2 on 2024-10-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0006_alter_products_uom_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]