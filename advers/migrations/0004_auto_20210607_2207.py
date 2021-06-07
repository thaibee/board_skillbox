# Generated by Django 3.1.11 on 2021-06-07 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advers', '0003_auto_20210607_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('f_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Телефонный номер')),
                ('email', models.CharField(max_length=50, verbose_name='Электронная почта')),
            ],
        ),
        migrations.AlterField(
            model_name='adver',
            name='description',
            field=models.TextField(verbose_name='Текст объявления'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advers', to='advers.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='title',
            field=models.CharField(max_length=1500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='adver',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advers', to='advers.type', verbose_name='Тип'),
        ),
    ]
