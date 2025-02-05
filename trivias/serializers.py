from rest_framework import serializers
from .models import Trivia

class TriviaSerializer(serializers.ModelSerializer):
    """ ModelSerializer class """
    class Meta:
        """ ModelSerializer Meta """
        model = Trivia
        fields = ['id', 'name', 'description', 'questions', 'users']
