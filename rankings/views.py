from django.shortcuts import render
from rest_framework import viewsets
from .models import Ranking
from .serializers import RankingSerializer
from rest_framework.permissions import IsAuthenticated

class RankingViewSet(viewsets.ModelViewSet):
    """ Class RankingViewSet"""
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    permission_classes = [IsAuthenticated]
    