from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import (
    StudyMemo, Profile, Language
)
from .forms import(
    ProfileForm
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

def set_profile(request):
    if (request.method == 'POST'):
        user = User.objects.first()
        language = Language.objects.filter(id=request.POST['language']).first()
        profile = Profile()
        profile.owner = user
        profile.language = language
        profile.study_start_at = request.POST['study_start_at']
        profile.introduction = request.POST['introduction']
        profile.save()
        return redirect(to='/engineer')
    params = {
        'form': ProfileForm()
    }
    return render(request, 'engineer/set_profile.html', params)

def edit_profile(request, num):
    user = User.objects.get(id=num)
    profile = Profile.objects.get(owner=user.id)
    if (request.method == 'POST'):
        language = Language.objects.filter(id=request.POST['language']).first()
        profile.owner = user
        profile.language = language
        profile.study_start_at = request.POST['study_start_at']
        profile.introduction = request.POST['introduction']
        profile.save()
        return redirect(to='/engineer')
    params = {
        'id': num,
        'form': ProfileForm(instance=profile),
    }
    return render(request, 'engineer/edit_profile.html', params)