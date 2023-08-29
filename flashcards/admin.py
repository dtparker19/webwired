from django.contrib import admin
from .models import Flashcard, FlashcardTopic, FlashcardDifficulty

@admin.register(FlashcardTopic)
class FlashcardTopicAdmin(admin.ModelAdmin):
    pass

@admin.register(FlashcardDifficulty)
class FlashcardDifficultyAdmin(admin.ModelAdmin):
    pass

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['question', 'topic', 'difficulty', 'created_by', 'created_at']
