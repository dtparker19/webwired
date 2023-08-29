from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['topic', 'difficulty', 'question', 'answer', 'ai_generated_explanation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Flashcard'))
