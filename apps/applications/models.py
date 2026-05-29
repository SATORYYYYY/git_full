from django.db import models
from apps.users.models import User


class Zayavka(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'Идет обучение'),
        ('completed', 'Обучение завершено'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Наличными'),
        ('transfer', 'Перевод по номеру телефона'),
    ]

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
