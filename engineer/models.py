from django.db import models
from django.contrib.auth.models import User


class StudyMemo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_memo_owner')
    title = models.TextField(max_length=30)
    memo = models.TextField(max_length=140)
    time = models.IntegerField(default=30)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + ': ' + str(self.title)


class Language(models.Model):
    name = models.TextField()

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='profile_language')
    study_start_at = models.DateField()

    def __str__(self):
        return str(self.owner)