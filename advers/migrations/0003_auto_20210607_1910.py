# Generated by Django 3.1.11 on 2021-06-07 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advers', '0002_auto_20210607_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adver',
            options={'ordering': ['title']},
        ),
    ]
