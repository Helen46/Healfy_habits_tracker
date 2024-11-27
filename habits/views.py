from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """CRUD для привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
       habit = serializer.save(owner=self.request.user)
       habit.save()

    def get_permissions(self):
        if self.action == "list" and Habit.objects.filter(is_published=True):
            return self.permission_classes == (IsAuthenticated,)
        else:
            return self.permission_classes == (IsOwner,)

