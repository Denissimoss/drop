# Generated by Django 4.0.5 on 2022-06-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_book_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.CharField(default=1, max_length=5, verbose_name='number'),
            preserve_default=False,
        ),
    ]
