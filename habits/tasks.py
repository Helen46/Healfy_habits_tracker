# from datetime import datetime
#
# from celery import shared_task
#
# from habits.models import Habit
#
#
# @shared_task
# def send_info_obout_start_habit():
#     """
#     Отправка информации на Телеграм о старте привычки
#     :return:
#     """
#
#     time_now = datetime.now().time()
#     habits = Habit.oblects.all()
#
#     for habit in habits:
#         if habit.start_time >= time_now:
#
