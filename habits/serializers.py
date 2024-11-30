from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import RelatedHabitOrRewordValidator, CheckLeadTimeValidator, RelatedHabitNotPleasantValidator, \
    IsPleasantNotRelatedHabitOrRewordValidator


class HabitSerializer(ModelSerializer):
    """
    Сериализатор вывода привычки
    """
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedHabitOrRewordValidator(field_1="related_habit", field_2="reward"),
            CheckLeadTimeValidator(field="lead_time"),
            RelatedHabitNotPleasantValidator(field_1="related_habit", field_2="is_pleasant"),
            IsPleasantNotRelatedHabitOrRewordValidator(field_1="is_pleasant", field_2="related_habit", field_3="reward")
        ]
