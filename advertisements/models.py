from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    crt_time = models.DateTimeField(auto_now_add=True)
    upd_time = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена продукта', default=0)
    view_cnt = models.IntegerField(verbose_name='Счетчик просмотров', default=0)
