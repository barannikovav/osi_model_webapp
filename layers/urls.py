from django.urls import path

from . import views

app_name = "layers"
urlpatterns = [
    # ex: /layers/
    path("", views.index, name="index"),
    # ex: /layers/2/
    path("<int:layer_id>/", views.detail, name="detail"),
    # ex: /layers/2/test/
    path("<int:question_id>/test/", views.test, name="test"),
]