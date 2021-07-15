from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='E-mail',
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        blank=False,
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=False,
        max_length=150,
    )

    #USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
