from django.db import models


class User(models.Model):

    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)

    def check_password(self, password):
        return self.u_password == password


class Blog(models.Model):
    b_title = models.CharField(max_length=128)
    b_content = models.TextField()
    b_author = models.ForeignKey(User)


class Address(models.Model):
    a_address = models.CharField(max_length=128)
    a_user = models.ForeignKey(User)