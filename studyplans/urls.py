from django.urls import path
from . import views

urlpatterns = [
    path('studyplans/<int:studyplan_id>/', views.studyplan_detail, name='studyplan_detail'),
]
