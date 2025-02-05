from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Пользователь {self.user.username}'
    
    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
