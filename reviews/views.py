'''reviews Django app views configuration'''
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
def index(request):
    '''Page with reviews list'''
    feedbacks = Feedback.objects.order_by('-created_at')[:10]

    return render(request, 'reviews/index.html', {'reviews': feedbacks})

def add_review(request):
    '''Page for adding review'''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за ваш отзыв!')
            return redirect('reviews:add')
    else:
        form = FeedbackForm()

    return render(request, 'reviews/add.html', {'form': form})
