from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    class Subjects(models.IntegerChoices):
        WEB_DEV=1
        PROGRAMMING = 2
        DATA = 3

    subject = models.PositiveSmallIntegerField(choices=Subjects.choices)
    dob = models.DateField()