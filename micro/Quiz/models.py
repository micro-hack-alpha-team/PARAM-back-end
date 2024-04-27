from django.db import models
from user.models import User


class Question(models.Model):
    text = models.TextField()

class PossibleAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='possible_answers')
    text = models.TextField()

class SelectedAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE)
    
    class Meta:
       unique_together = (('user', 'question'),)

       