from django.db import models
from jsonfield import JSONField

# Create your models here.


class Inventory(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class LoadFile(models.Model):
    file_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    file = models.FileField()
    jfile = JSONField(null=True, blank=True)
