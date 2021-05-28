from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)
    question_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class AllAnswers(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255, )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
