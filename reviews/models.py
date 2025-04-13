'''reviews Django app models configuration'''
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    '''Feedback model for review app'''
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    email = models.EmailField(verbose_name='Email')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка (1-5)'
    )
    message = models.TextField(verbose_name='Ваш отзыв')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Отзыв от {self.name} ({self.rating}/5)'
