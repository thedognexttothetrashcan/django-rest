from django.db import models


class Animal(models.Model):

    a_name = models.CharField(max_length=32)
    a_weight = models.FloatField(default=10)


class Spider(models.Model):

    s_host = models.CharField(max_length=200)


class People(models.Model):

    p_name = models.CharField(max_length=32)
    p_age = models.IntegerField(default=18)