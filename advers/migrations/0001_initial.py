# Generated by Django 3.1.11 on 2021-06-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Adver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500)),
                ('description', models.TextField()),
                ('crt_time', models.DateTimeField(auto_now_add=True)),
                ('upd_time', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0, verbose_name='цена продукта')),
                ('view_cnt', models.IntegerField(default=0, verbose_name='Счетчик просмотров')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advers', to='advers.status')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advers', to='advers.type')),
            ],
        ),
    ]