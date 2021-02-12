from django.shortcuts import render
from django.http import HttpResponse
from .models import StudyMemo

def index(request):
    data = StudyMemo.objects.filter(is_public=True)
    params = {
        'data': data
    }
    return render(request, 'engineer/index.html', params)
