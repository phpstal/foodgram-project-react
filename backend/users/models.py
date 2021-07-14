from django.db import models
from django.contrib.auth.models import AbstractUser


class ROLES_CHOICES(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class FoodUser(AbstractUser):
    id = models.AutoField(
        primary_key=True, 
        db_index=True
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Логин пользователя',
        blank=False,
        unique=True,
    )
    password = models.CharField(
        max_length=70,
        verbose_name='Пароль пользователя',
        blank=False,
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='E-Mail', 
        unique=True,
        blank=False
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        blank=False,
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        blank=False,
    )

    role = models.CharField(
        default=ROLES_CHOICES.USER,
        max_length=100,
        choices=ROLES_CHOICES.choices,
        verbose_name='Роль пользователя',
    )
    user_permissions = None
    groups = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    @property
    def is_admin(self):
        return any([
            self.role == ROLES_CHOICES.ADMIN,
            self.is_superuser,
            self.is_staff,
        ])

    @property
    def is_moderator(self):
        return self.role == ROLES_CHOICES.MODERATOR

    class Meta:
        verbose_name_plural = 'Пользователи'
        ordering = ['id']