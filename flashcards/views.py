from django.shortcuts import render, redirect
from .models import Flashcard
from .forms import FlashcardForm

def create_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.created_by = request.user  # Assign the logged-in user as the creator
            flashcard.save()
            return redirect('flashcards_list')  # Redirect to the flashcards list view
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/create_flashcard.html', {'form': form})

def flashcards_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/flashcards_list.html', {'flashcards': flashcards})

def flashcard_detail(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    return render(request, 'flashcards/flashcard_detail.html', {'flashcard': flashcard})

