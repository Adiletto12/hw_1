from django.urls import path
from . import views

urlpatterns = [
    path('rezka_films/', views.RezkaListView.as_view()),
    path('film_parser/', views.GetParsing.as_view()),
]