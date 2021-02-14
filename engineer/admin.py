from django.contrib import admin
from .models import (
    StudyMemo, Language, Profile, Book
)


admin.site.register(StudyMemo)
admin.site.register(Language)
admin.site.register(Profile)
admin.site.register(Book)
