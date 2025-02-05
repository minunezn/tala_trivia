from rest_framework import serializers
from .models import Ranking

class RankingSerializer(serializers.ModelSerializer):
    """ Ranking Serializer """
    class Meta:
        """ Class Meta Ranking Serializer """
        model = Ranking
        fields = ['user', 'trivia', 'score', 'rank']
