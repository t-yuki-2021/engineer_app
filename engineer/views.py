from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    StudyMemo, Profile
)


def index(request):
    data = StudyMemo.objects.filter(is_public=True)
    params = {
        'data': data
    }
    return render(request, 'engineer/index.html', params)

def users(request):
    data = Profile.objects.all()
    params = {
        'data': data
    }
    return render(request, 'engineer/users.html', params)