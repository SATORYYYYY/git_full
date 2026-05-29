from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fio = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
