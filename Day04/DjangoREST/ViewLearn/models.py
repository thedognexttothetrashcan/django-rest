from django.db import models


class Computer(models.Model):

    c_name = models.CharField(max_length=16)
    c_price = models.FloatField(default=1)