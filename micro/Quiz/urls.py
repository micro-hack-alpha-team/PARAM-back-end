
from django.urls import include, re_path , path
from .views import SendQuiz

urlpatterns = [
	re_path(r'^getquiz/?$', SendQuiz.as_view()),]