# Generated by Django 5.1.2 on 2024-10-19 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderDetail",
            new_name="OrderDetails",
        ),
        migrations.RenameModel(
            old_name="Order",
            new_name="Orders",
        ),
        migrations.RenameModel(
            old_name="Product",
            new_name="Products",
        ),
    ]