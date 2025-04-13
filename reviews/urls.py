'''reviews Django app URL Configuration'''
from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
    # ex: /reviews/
    path("", views.index, name="index"),
    # ex: /layers/add/
    path("add/", views.add_review, name="add"),
]
