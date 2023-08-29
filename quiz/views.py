from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, UserQuizAttempt, Question, Answer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    unanswered_questions = get_unanswered_questions(request.user, quiz)
    
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer_id = request.POST.get('selected_answer')
        update_user_progress(request.user, question_id, selected_answer_id, quiz)
        return redirect('quiz/quiz_detail', quiz_id=quiz_id)
    
    if unanswered_questions:
        question = unanswered_questions[0]
    else:
        question = None
    
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'question': question})

def get_unanswered_questions(user, quiz):
    answered_question_ids = user.userquizattempt_set.filter(quiz=quiz).values_list('answered_questions', flat=True)
    unanswered_questions = quiz.question_set.exclude(id__in=answered_question_ids)
    return unanswered_questions

def update_user_progress(user, question_id, selected_answer_id, quiz):
    question = Question.objects.get(id=question_id)
    selected_answer = Answer.objects.get(id=selected_answer_id)
    
    attempt, created = UserQuizAttempt.objects.get_or_create(user=user, quiz=quiz)
    attempt.answered_questions.add(question)
    
    if selected_answer.is_correct:
        attempt.score += 1
    attempt.save()
