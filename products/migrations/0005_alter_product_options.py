# Generated by Django 4.0.5 on 2022-07-08 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]