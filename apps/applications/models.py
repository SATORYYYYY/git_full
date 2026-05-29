from django.db import models
<<<<<<< HEAD
from apps.users.models import User


class Zayavka(models.Model):
=======
from apps.users.models import CustomUser

class Application(models.Model):
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'Идет обучение'),
        ('completed', 'Обучение завершено'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Наличными'),
        ('transfer', 'Перевод по номеру телефона'),
    ]

<<<<<<< HEAD
    polzovatel = models.ForeignKey(User, on_delete=models.CASCADE)
    kurs = models.CharField(max_length=100)
    data_nachala = models.CharField(max_length=10)
    oplata = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    otzyv = models.TextField(blank=True, null=True)
    sozdan = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'applications_zayavka'

    def __str__(self):
        return f"{self.kurs} - {self.polzovatel.username}"
=======
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)  
    start_date = models.CharField(max_length=10)  
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course} - {self.user.username}"
# Create your models here.
>>>>>>> 3dc41b8156e7404e074383ad3ee1b8df3b6dc39f
