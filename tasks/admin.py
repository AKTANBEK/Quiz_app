from django.contrib import admin
from .models import Question, AllAnswers


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(AllAnswers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'is_correct']

