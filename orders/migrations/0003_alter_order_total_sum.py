# Generated by Django 4.0.5 on 2022-07-08 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
