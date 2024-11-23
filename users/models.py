from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите ваш email",
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите ваше имя",
        **NULLABLE,
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
        **NULLABLE,
    )

    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE,
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Введите ваш номер телефона",
        **NULLABLE,
    )

    tg_nick = models.CharField(
        max_length=35,
        verbose_name="Телеграм ник",
        help_text="Введите ваш телеграм ник",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
