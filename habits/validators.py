from rest_framework.exceptions import ValidationError


class RelatedHabitOrRewordValidator:
    """
    Валидатор использования одновременно связанной привычки и вознаграждения
    """
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)
        reward = dict(value).get(self.field_2)

        if related_habit and reward:
            raise ValidationError('Нельзя использовать одновременно связанную привычку и вознаграждение')


class CheckLeadTimeValidator:
    """
    Валидатор времени выполнения привычки
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        lead_time = dict(value).get(self.field)

        if int(lead_time) > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 минут")


class RelatedHabitNotPleasantValidator:
    """
    Валидатор связанной привычки как приятной
    """
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)
        is_pleasant = dict(value).get(self.field_2)

        if related_habit and not is_pleasant:
            raise ValidationError("Свяанная привычка должна быть приятной")


class IsPleasantNotRelatedHabitOrRewordValidator:
    """
    Валидатор наличия у приятной привычки связанной привычки или вознаграждения
    """
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        is_pleasant = dict(value).get(self.field_1)
        related_habit = dict(value).get(self.field_2)
        reward = dict(value).get(self.field_2)

        if (is_pleasant and related_habit) or (is_pleasant and reward):
            raise ValidationError("У приятной привычки не может быть связанной привычки или вознаграждения")
