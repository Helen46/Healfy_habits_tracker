import datetime

import pytz
from celery import shared_task

from config import settings
from habits.models import Habit
from habits.services import send_telegram_message

PERIOD_TIMEDELTA = {
    'every day': datetime.timedelta(days=1),
    'every other day': datetime.timedelta(days=2),
    'every three days': datetime.timedelta(days=3),
    'every four days': datetime.timedelta(days=4),
    'every five days': datetime.timedelta(days=5),
    'every six days': datetime.timedelta(days=6),
    'every weak': datetime.timedelta(weeks=1)
    }

@shared_task
def check_habits():
    """
    Периодическая задача
    """
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.datetime.now(zone)
    habits = Habit.objects.filter(owner__tg_nick__isnull=False)
    for habit in habits:
        if habit.start_time <= now:
            user_tg = habit.owner.tg_nick
            if habit.place:
                message = f"Пришло время {habit.action} в {habit.place}"
            else:
                message = f"Пришло время {habit.action}"
            send_telegram_message(user_tg, message)
            habit.start_time += PERIOD_TIMEDELTA
