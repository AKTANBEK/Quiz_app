from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks.models import Question


class User(AbstractUser):
    email = models.EmailField()
    score = models.PositiveIntegerField()
    questions = models.ManyToManyField(Question, related_name='questions')
    completed_test = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)
