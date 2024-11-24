from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """CRUD для привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
