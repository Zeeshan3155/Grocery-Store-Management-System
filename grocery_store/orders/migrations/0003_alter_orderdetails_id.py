# Generated by Django 5.1.2 on 2024-10-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_rename_orderdetail_orderdetails_rename_order_orders_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetails",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]