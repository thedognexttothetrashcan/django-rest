from django.db import models


class Book(models.Model):

    b_name = models.CharField(max_length=16)
    b_price = models.FloatField(default=1)