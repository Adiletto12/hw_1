from django.urls import path
from . import views

urlpatterns = [
    path('mashina_cars', views.MashinaListView.as_view()),
    path('cars_parser', views.GetParsingM3.as_view())
]