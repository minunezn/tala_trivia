from django.db import models
from questions.models import Question
from users.models import User

class Trivia(models.Model):
    """ Class trivias"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    