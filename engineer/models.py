from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.TextField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='book_language')
    name = models.TextField(max_length=100, null=True)
    memo = models.TextField(max_length=300,  null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.owner) + str(self.name)


class StudyMemo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_memo_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='study_memo_book', null=True)
    title = models.TextField(max_length=30)
    memo = models.TextField(max_length=140)
    time = models.IntegerField(default=30)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + ': ' + str(self.title)




class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_owner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='profile_language')
    study_start_at = models.DateField()
    introduction = models.TextField(max_length=300, null=True)

    def __str__(self):
        return str(self.owner)

