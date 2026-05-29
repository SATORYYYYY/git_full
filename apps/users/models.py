from django.contrib.auth.models import AbstractUser
from django.db import models

<<<<<<< HEAD

class User(AbstractUser):
    fio = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
=======
# Такого количества инфы нам вполне достаточно

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100) # фио
    phone = models.CharField(max_length=20) # телефон
    email = models.EmailField(unique=True)  # email 

# Create your models here.
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
