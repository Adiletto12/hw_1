from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
class CustomUserCreationForm(UserCreationForm):
    surname = forms.CharField()
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    height = forms.FloatField()
    age = forms.IntegerField()
    city = forms.CharField()
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996')
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))
    married = forms.BooleanField()


    class Meta:
        model = models.CustomUser
        fields = ('username',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'surname',
                  'date_of_birth',
                  'age',
                  'height',
                  'city',
                  'email',
                  'phone_number',
                  'gender',
                  'married')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.age = self.cleaned_data['age']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
            return user