# Generated by Django 3.1.2 on 2020-10-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='margem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='unit_price_sell',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
