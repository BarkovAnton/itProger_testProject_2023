from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UsersUrls(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    url_large = models.URLField('Длинная ссылка', max_length=100)
    url_small = models.CharField('Сокращенная ссылка', max_length=20)


    def __str__(self):
        return f'Ссылка {self.url_small} (пользователь {self.user})' 
    
    def get_absolute_url(self):
        return reverse('urlsadd')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'url_small'], name='unique')
        ]

        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'



