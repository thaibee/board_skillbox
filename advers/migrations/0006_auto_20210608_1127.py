# Generated by Django 3.1.11 on 2021-06-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advers', '0005_adver_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='birthday',
            field=models.DateField(default='1990-01-01', verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Электронная почта'),
        ),
    ]