# Generated by Django 4.2 on 2023-08-27 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flashcards", "0001_initial"),
        ("studyplans", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudyPlanStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_flashcards", models.PositiveIntegerField(default=0)),
                ("learned_flashcards", models.PositiveIntegerField(default=0)),
                ("correct_responses", models.PositiveIntegerField(default=0)),
                ("incorrect_responses", models.PositiveIntegerField(default=0)),
                (
                    "average_time_per_flashcard",
                    models.DurationField(blank=True, null=True),
                ),
                (
                    "study_plan",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studyplans.studyplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudyPlanRecommendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recommended_topics",
                    models.ManyToManyField(to="flashcards.flashcardtopic"),
                ),
                (
                    "study_plan",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studyplans.studyplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudyPlanFeedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("feedback_text", models.TextField()),
                ("feedback_date", models.DateTimeField(auto_now_add=True)),
                (
                    "study_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studyplans.studyplan",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
