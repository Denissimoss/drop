# Generated by Django 4.0.5 on 2022-06-21 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_book_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
