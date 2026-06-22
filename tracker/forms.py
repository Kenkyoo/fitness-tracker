from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ['activity', 'duration', 'date']
        widgets = {
            'activity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Running, Cycling, Yoga…',
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '30',
                'min': '1',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }