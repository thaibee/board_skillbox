import uuid
from django.db import models
from djmoney.models.fields import MoneyField


class UniqueIdentifierField(models.UUIDField):

    def db_type(self, connection):
        if self.primary_key:
            return 'uniqueidentifier default (newsequentialid())'
        else:
            return 'uniqueidentifier'

    def rel_db_type(self, connection):
        return 'uniqueidentifier'

    # leave id out of payload on insert
    def contribute_to_class(self, cls, name, **kwargs):
        assert not self.primary_key or (
                self.primary_key and not cls._meta.auto_field), "A model can't have more than one AutoField."
        super().contribute_to_class(cls, name, **kwargs)
        if self.primary_key:
            cls._meta.auto_field = self

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, uuid.UUID):
            value = self.to_python(value)

        return str(value)

    def from_db_value(self, value, expression, connection):
        return self._to_uuid(value)

    def to_python(self, value):
        return self._to_uuid(value)

    def _to_uuid(self, value):
        if value is not None and not isinstance(value, uuid.UUID):
            try:
                return uuid.UUID(value)
            except (AttributeError, ValueError):
                raise exceptions.ValidationError(
                    self.error_messages['invalid'],
                    code='invalid',
                    params={'value': value},
                )
        return value


class UUIDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        super(models.UUIDField, self).__init__(*args, **kwargs)


class Testing(models.Model):
    id = UniqueIdentifierField(primary_key=True, max_length=36, editable=False, default=None)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        db_table = 'testing'

    def __str__(self):
        return self.name
