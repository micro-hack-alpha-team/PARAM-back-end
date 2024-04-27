from django.contrib import admin
from django.urls import include, re_path , path
from .views import MakeFlowChart

urlpatterns = [
	re_path(r'^makeflowchart/?$', MakeFlowChart.as_view()),]