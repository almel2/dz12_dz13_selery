import datetime
from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError

from django.utils import timezone


class UserForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(initial=timezone.now())

    def clean_date(self):
        date = self.cleaned_data['date']

        if date > (timezone.now() + datetime.timedelta(days=2)) or date < timezone.now():
            raise ValidationError('Wrong date!')


class PlusForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
