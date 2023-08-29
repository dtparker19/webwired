from django.contrib import admin
from .models import StudyPlan, StudyPlanFlashcard, StudyPlanStatistics, StudyPlanRecommendation, StudyPlanFeedback

@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'target_certification', 'start_date', 'end_date', 'daily_study_time', 'active']

@admin.register(StudyPlanFlashcard)
class StudyPlanFlashcardAdmin(admin.ModelAdmin):
    list_display = ['study_plan', 'flashcard', 'learned', 'last_reviewed']

@admin.register(StudyPlanStatistics)
class StudyPlanStatisticsAdmin(admin.ModelAdmin):
    list_display = ['study_plan', 'total_flashcards', 'learned_flashcards', 'correct_responses', 'incorrect_responses', 'average_time_per_flashcard']

@admin.register(StudyPlanRecommendation)
class StudyPlanRecommendationAdmin(admin.ModelAdmin):
    list_display = ['study_plan']

@admin.register(StudyPlanFeedback)
class StudyPlanFeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'study_plan', 'feedback_date']
