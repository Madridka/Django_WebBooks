from django import forms
from django.forms import ModelForm
from .models import Book

from datetime import date


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    birth_date = forms.DateField(label='Дата рождения',
                                 initial=format(date.today()),
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    death_date = forms.DateField(label='Дата смерти',
                                 initial=format(date.today()),
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']
