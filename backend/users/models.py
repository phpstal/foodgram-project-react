from django.contrib.auth.models import AbstractUser
from django.db import models


class ROLES_CHOICES(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


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
    role = models.CharField(
        default=ROLES_CHOICES.ADMIN,
        max_length=100,
        choices=ROLES_CHOICES.choices,
        verbose_name='Роль пользователя',
    )

    REQUIRED_FIELDS = ('email', 'first_name', 'last_name')

    @property
    def is_admin(self):
        return any([
            self.role == ROLES_CHOICES.ADMIN,
            self.is_superuser,
            self.is_staff,
        ])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', )

    def __str__(self):
        return self.username