# streakpy/models.py
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def calculate_streak(self):
        completions = self.habitcompletion_set.order_by('-completed_at')
        if not completions:
            return 0

        streak = 0
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
class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['habit', 'completed_at']