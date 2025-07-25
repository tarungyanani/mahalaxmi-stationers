# Generated by Django 5.2.4 on 2025-07-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='mrp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='MRP'),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Selling Price'),
        ),
    ]
