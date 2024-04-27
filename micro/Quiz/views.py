from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question , PossibleAnswer 
from .serializers import QuestionSerializer , PossibleAnswerSerializer
from django.http import JsonResponse
# Create your views here.

class SendQuiz(APIView):
    def get(self , request):
        questionset = Question.objects.all()
        questionserializer = QuestionSerializer(questionset, many = True)
        possibleset = PossibleAnswer.objects.all()
        possibleserializer = PossibleAnswerSerializer(possibleset, many = True)
        questions = questionserializer.data
        possibleAnswers = possibleserializer.data
        return JsonResponse({questions,possibleAnswers}, safe=False)

    

