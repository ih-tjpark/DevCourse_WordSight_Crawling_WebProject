from django import forms
from .models import *
from django.forms import ModelForm, DateInput
#class InterestChoicesForm(forms.Form):
#    tag = forms.MultipleChoiceField(
#        required=False,
#        widget=forms.CheckboxSelectMultiple,
#        queryset=TagInterest.objects.all(),
#        label="interest_category",
#    )
