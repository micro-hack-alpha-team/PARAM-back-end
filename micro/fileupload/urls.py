from django.urls import re_path
from .views import UploadArticleViaFile

urlpatterns = [
	re_path(r'^upload/?$', UploadArticleViaFile.as_view()),
]