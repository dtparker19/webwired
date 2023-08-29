from django.db import models
from accounts.models import CustomUser
# Create your models here.

from taggit.managers import TaggableManager

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Other quiz-related fields

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    # Other question-related fields

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    # Other answer-related fields

class UserQuizAttempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    answered_questions = models.ManyToManyField(Question)
