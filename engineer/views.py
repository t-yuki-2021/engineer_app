from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import (
    StudyMemo, Profile, Language, Book
)
from .forms import(
    ProfileForm, BookForm, StudyMemoForm
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

def register_book(request):
    if (request.method == 'POST'):
        user = User.objects.first()
        language = Language.objects.filter(id=request.POST['language']).first()
        book = Book()
        book.owner = user
        book.language = language
        book.name = request.POST['name']
        book.price = request.POST['price']
        book.memo = request.POST['memo']
        book.save()
        return redirect(to='/engineer')
    params = {
        'form': BookForm()
    }
    return render(request, 'engineer/register_book.html', params)

def register_study(request, num, is_public):
    user = User.objects.get(id=num)
    if (request.method == 'POST'):
        book = Book.objects.filter(id=request.POST['book']).first()
        study_memo = StudyMemo()
        study_memo.owner = user
        study_memo.book = book
        study_memo.title = request.POST['title']
        study_memo.memo = request.POST['memo']
        study_memo.time = request.POST['time']
        study_memo.is_public = is_public
        study_memo.save()
        return redirect(to='/engineer')
    params = {
        'id': num,
        'form': StudyMemoForm(),
    }
    return render(request, 'engineer/study_memo.html', params)

    memo = models.TextField(max_length=140)
    time = models.IntegerField(default=30)
    is_public = models.BooleanField(default=False)