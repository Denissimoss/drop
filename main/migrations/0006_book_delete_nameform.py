# Generated by Django 4.0.5 on 2022-06-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_nameform_options_remove_nameform_qw_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='name')),
                ('author', models.CharField(max_length=5, verbose_name='author')),
            ],
            options={
                'verbose_name': 'book',
            },
        ),
        migrations.DeleteModel(
            name='NameForm',
        ),
    ]