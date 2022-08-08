# Generated by Django 4.0 on 2022-03-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_nameform_yourname_nameform_qw'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nameform',
            options={'verbose_name': 'book'},
        ),
        migrations.RemoveField(
            model_name='nameform',
            name='qw',
        ),
        migrations.AddField(
            model_name='nameform',
            name='author',
            field=models.CharField(default=1, max_length=5, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nameform',
            name='name',
            field=models.CharField(default='den', max_length=5, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nameform',
            name='number',
            field=models.CharField(default=234, max_length=5, verbose_name='number'),
            preserve_default=False,
        ),
    ]