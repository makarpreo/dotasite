from django import forms
from .models import *

HERO_CHOICES = [
    ('', ''),
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
]


class UserForm(forms.ModelForm):
    class Meta:
        model = Heroes
        fields = ['first_hero', 'second_hero', 'third_hero', 'fourth_hero']