from rest_framework import serializers
from .models import Question,PossibleAnswer,SelectedAnswer
"""
	TODO documentation.
"""
class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'
		
class PossibleAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = PossibleAnswer
		fields = '__all__'        
		
class SelectedAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = SelectedAnswer
		fields = '__all__'          