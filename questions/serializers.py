from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    """ Class Serializer of question"""

    class Meta:
        """ Class Meta of question"""
        model = Question
        fields = '__all__'
        extra_kwargs = {'correct_answer': {'write_only': True}, 'difficulty': {'write_only': True}}
