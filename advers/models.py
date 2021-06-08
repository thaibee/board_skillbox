import uuid as uuid
from django.db import models


class Adver(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Описание')
    description = models.TextField(verbose_name='Текст объявления')
    crt_time = models.DateTimeField(auto_now_add=True)
    upd_time = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена продукта', default=0)
    view_cnt = models.IntegerField(verbose_name='Счетчик просмотров', default=0)
    status = models.ForeignKey('Status', default=None, null=True, on_delete=models.CASCADE, related_name='advers',
                               verbose_name='Статус')
    type = models.ForeignKey('Type', default=None, null=True, on_delete=models.CASCADE, related_name='advers',
                             verbose_name='Тип')
    owner = models.ForeignKey('Owner', default=None, null=True, on_delete=models.CASCADE, related_name='advers',
                              verbose_name='Владелец')

    class Meta:
        db_table = 'adveris'
        ordering = ['title']

    def __str__(self):
        return self.title


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Owner(models.Model):
    l_name = models.CharField(max_length=50, verbose_name='Фамилия')
    f_name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, verbose_name='Телефонный номер')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    birthday = models.DateField(verbose_name='Дата рождения')
    #uuid = models.UUIDField(editable=False, default=uuid, unique=True)

    def __str__(self):
        return self.l_name + ' ' + self.f_name

