# streakpy/models.py
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def get_last_10_days(self):
        today = timezone.now().date()
        last_10_days = [(today - timezone.timedelta(days=i)) for i in range(10)]
        completions = self.habitcompletion_set.filter(completed_at__in=last_10_days)
        completion_dates = {completion.completed_at for completion in completions}

        return [
            {'date': day, 'completed': day in completion_dates}
            for day in last_10_days
        ]

    def calculate_streak(self):
        completions = self.habitcompletion_set.order_by('-completed_at')
        if not completions:
            return 0

        streak = 1
        latest = completions[0].completed_at

        for completion in completions:
            if completion.completed_at == latest - timezone.timedelta(days=1):
                streak += 1
                latest = completion.completed_at
            else:
                break

        return streak

    def __str__(self):
        return self.name
from django.db.models import UniqueConstraint

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateField(auto_now_add=True)
    #is_completed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'completed_at'], name='unique_habit_completion')
        ]
