from django.db import models

from users.querysets import PersonQuerySet


class Person(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    work = models.CharField(max_length=256)
    age = models.IntegerField()

    # objects = PersonQuerySet.as_manager()