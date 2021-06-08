import uuid
from django.db import models
from djmoney.models.fields import MoneyField


class UUIDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        super(models.UUIDField, self).__init__(*args, **kwargs)


class Testing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    id2 = models.UUIDField(default=uuid.uuid4, editable=False, max_length=36)

