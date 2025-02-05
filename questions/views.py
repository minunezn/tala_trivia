from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin

class QuestionViewSet(viewsets.ModelViewSet):
    """ class """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


    def list(self, request):
        """ GET List """
        print("List", request)
        return super().list(request)

    def create(self, request):
        """ POST create """
        print("create", request)
        return super().create(request)

    def retrieve(self, request, pk=None): 
        """ GET retrieve """
        print("retrieve", request)
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        """ PUT update"""
        print("update", request)
        return super().update(request, pk)
