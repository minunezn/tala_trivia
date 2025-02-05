from django.shortcuts import render
from rest_framework import viewsets
from users.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsPlayer
from questions.models import Question
from rankings.models import Ranking
from .models import Trivia
from .serializers import TriviaSerializer

class TriviaViewSet(viewsets.ModelViewSet):
    """ Class TriviaViewSet"""
    queryset = Trivia.objects.all()
    serializer_class = TriviaSerializer
    permission_classes = [IsAuthenticated]

    def answer_question(self, request, trivia_id, question_id):
        """ Function to answer question """
        trivia = Trivia.objects.get(id=trivia_id)
        question = Question.objects.get(id=question_id)
        trivia_instance = Trivia.objects.get(id=trivia.id)

        user = request.user
        answer = request.data.get('answer')
        points = 0

        print('answer == question.correct_answer', answer, question.correct_answer)

        if answer == question.correct_answer:
            difficulty = self.difficulty_to_text(question.difficulty)

            if difficulty == 'easy':
                points = 1
            elif difficulty == 'medium':
                points = 2
            elif difficulty == 'hard':
                points = 3

            if points > 0:
                ranking = Ranking.objects.filter(user=user, trivia=trivia_instance).first()

                if ranking:
                    ranking.score += points
                else:
                    ranking = Ranking(user=user, trivia=trivia_instance, score=points)

                ranking.save()

                return Response({'status': 'correct', 'points': points})

            return Response({'status': 'incorrect', 'message': 'Invalid points'}, status=400)

        return Response({'status': 'incorrect'}, status=400)

    def difficulty_to_text(self, difficulty):
        """ Funtion to convert num to text"""
        if difficulty == '1':
            difficulty = 'easy'
        elif difficulty == '2':
            difficulty = 'medium'
        elif difficulty == '3':
            difficulty = 'hard'
        return difficulty
