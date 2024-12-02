from django.db import models

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    """
    Модель привычки
    """

    RHYTHM_CHOICES = [
        ("every day", "каждый день"),
        ("every other day", "чере день"),
        ("every three days", "раз в 3 дня"),
        ("every four days", "раз в 4 дня"),
        ("every five days", "раз в 5 дней"),
        ("every six days", "ра в 6 дней"),
        ("every weak", "раз в неделю")
    ]
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        **NULLABLE
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место выполнения привычки",
        **NULLABLE,
    )
    start_time = models.DateTimeField(
        verbose_name="Время начала выполнения привычки",
        help_text="Выберете дату и время начала привычки",
        **NULLABLE
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие привычки",
        help_text="Опишите действие вашей привычки",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка является приятной",
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Выбирите связанную приятную привычку",
        **NULLABLE,
    )
    rhythm = models.CharField(
        max_length=16,
        choices=RHYTHM_CHOICES,
        verbose_name="Переодичность выполнения",
        help_text="Выберите переодичностьт выполнения привычки",
    )
    reward = models.CharField(
        max_length=300,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
        **NULLABLE,
    )
    lead_time = models.IntegerField(
        default=1,
        verbose_name="Время выполнения",
        help_text="Укажите предположительное время выполнения привычки в минутах",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Общий доступ",
        help_text="Опубликовать для общего доступа",
    )

