from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your additional fields for learning progress statistics here
    #total_correct_responses = models.PositiveIntegerField(default=0)
    #total_incorrect_responses = models.PositiveIntegerField(default=0)
    #total_time_spent = models.DurationField(default=0)
    # ... other fields ...

    def __str__(self):
        return self.email