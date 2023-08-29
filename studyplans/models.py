from django.db import models
from flashcards.models import Flashcard
from accounts.models import CustomUser

class StudyPlan(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    target_certification = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    daily_study_time = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

class StudyPlanFlashcard(models.Model):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    learned = models.BooleanField(default=False)
    last_reviewed = models.DateTimeField(null=True, blank=True)

class StudyPlanStatistics(models.Model):
    study_plan = models.OneToOneField(StudyPlan, on_delete=models.CASCADE)
    total_flashcards = models.PositiveIntegerField(default=0)
    learned_flashcards = models.PositiveIntegerField(default=0)
    correct_responses = models.PositiveIntegerField(default=0)
    incorrect_responses = models.PositiveIntegerField(default=0)
    average_time_per_flashcard = models.DurationField(null=True, blank=True)
    # Add more relevant statistics as needed

class StudyPlanRecommendation(models.Model):
    study_plan = models.OneToOneField(StudyPlan, on_delete=models.CASCADE)
    recommended_topics = models.ManyToManyField('flashcards.FlashcardTopic')  # Assuming flashcards are in a separate app
    # Add more recommended resources or topics

class StudyPlanFeedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)

class FlashcardReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='FlashCardReviewUser')
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name='FlashCardReviewFlashcard')
    reviewed_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField()
    notes = models.TextField(blank=True, null=True)

class StudyPlanProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    progress_percentage = models.PositiveIntegerField()
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)




