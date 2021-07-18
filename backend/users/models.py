from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        blank=False, 
        max_length=254, 
        unique=True,
    )
    first_name = models.CharField(
        blank=False, 
        max_length=150,
    )
    last_name = models.CharField(
        blank=False, 
        max_length=150,
    )

    REQUIRED_FIELDS = ('email', 'first_name', 'last_name')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', )

    def __str__(self):
        return self.username