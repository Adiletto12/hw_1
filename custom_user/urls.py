from django.urls import path
from . import views

app_name = 'person'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.AuthorizationView.as_view(), name='login'),
    path('logout/', views.OutlogoutView.as_view(), name='logout'),
    path('person_list/', views.PersonListView.as_view(), name='person_list')
]