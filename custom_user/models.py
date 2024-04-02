from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    surname = models.TextField(max_length=40, null=True)
    age = models.IntegerField()
    height = models.FloatField()
    city = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=30, default="+996")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=(('M', 'Male'), ('F', 'Female')))
    married = models.BooleanField(default=False)

