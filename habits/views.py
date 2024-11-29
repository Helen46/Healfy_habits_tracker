from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """CRUD для привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = HabitsPagination

    def perform_create(self, serializer):
       habit = serializer.save(owner=self.request.user)
       habit.save()

    def get_permissions(self):
       if self.action != "create":
           self.permission_classes = (IsAuthenticated, IsOwner)
       return super().get_permissions()


class PublishedHabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsPagination
