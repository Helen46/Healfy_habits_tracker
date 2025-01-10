from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import PublishedHabitListAPIView, HabitViewSet

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [
   path('published_list/', PublishedHabitListAPIView.as_view(), name='published_list'),
]

urlpatterns += router.urls
