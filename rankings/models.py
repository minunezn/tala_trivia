from django.db import models
from users.models import User
from trivias.models import Trivia

class Ranking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.trivia.name}'

    class Meta:
        unique_together = ['user', 'trivia']

    @property
    def rank(self):
        """ metodo de Ranking"""
        rankings = Ranking.objects.filter(trivia=self.trivia).order_by('-score')
        return list(rankings).index(self) + 1
