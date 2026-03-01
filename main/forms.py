from django import forms
from .models import Lesson, Event

# Форма для урока
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'date', 'time', 'topic']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lesson Title'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-select'}),
        }

# Форма для события (Event)
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
        }
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class LanguageForm(forms.Form):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('uk', 'Ukrainian'),
    ]
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

