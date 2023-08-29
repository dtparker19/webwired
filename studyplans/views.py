from django.shortcuts import render, get_object_or_404
from .models import StudyPlan

def studyplan_detail(request, studyplan_id):
    study_plan = get_object_or_404(StudyPlan, id=studyplan_id)
    return render(request, 'studyplan_detail.html', {'study_plan': study_plan})
