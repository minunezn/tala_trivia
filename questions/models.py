from django.db import models

class Question(models.Model):
    """ Class Question """
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )

    question_text = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    correct_answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
