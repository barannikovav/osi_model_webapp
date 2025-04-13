'''reviews Django apps configuration'''
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    '''Config for reviews app'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
