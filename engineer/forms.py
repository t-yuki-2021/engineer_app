from django import forms
from .models import (
    Profile, Book, StudyMemo
)
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['language', 'study_start_at', 'introduction']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['language', 'name', 'price', 'memo']


class StudyMemoForm(forms.ModelForm):
    class Meta:
        model = StudyMemo
        fields = ['book', 'title', 'memo', 'time']