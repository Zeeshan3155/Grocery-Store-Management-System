# Generated by Django 5.1.2 on 2024-10-21 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_alter_products_uom_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="uom_id",
            field=models.ForeignKey(
                db_column="uom_id",
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="products",
                to="orders.uom",
            ),
        ),
    ]
