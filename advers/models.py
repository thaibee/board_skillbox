from django.db import models

class Adver(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    crt_time = models.DateTimeField(auto_now_add=True)
    upd_time = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена продукта', default=0)
    view_cnt = models.IntegerField(verbose_name='Счетчик просмотров', default=0)
    status = models.ForeignKey('Status', default=None, null=True, on_delete=models.CASCADE, related_name='advers')
    type = models.ForeignKey('Type', default=None, null=True, on_delete=models.CASCADE, related_name='advers')

    class Meta:
        db_table = 'adveris'
        ordering = ['title']


class Status(models.Model):
    name = models.CharField(max_length=30)


class Type(models.Model):
    name = models.CharField(max_length=30)
