'''reviews Django app forms configuration'''
from django import forms
from .models import Feedback

class  FeedbackForm(forms.ModelForm):
    '''Feedbac form for review app'''
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5
            }),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'name': 'Ваше имя',
            'email': 'Email для обратной связи',
            'rating': 'Оценка (от 1 до 5)',
            'message': 'Текст отзыва',
        }
