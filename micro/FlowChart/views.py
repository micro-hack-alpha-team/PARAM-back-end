from django.shortcuts import render
from rest_framework.views import APIView
from graphviz import Digraph
from .models import Actor , Document , AccessLog
# Create your views here.

class MakeFlowChart(APIView):
    def post(self , request , *args, **kwargs):
        owner = request.user
        print(owner)
        dot = Digraph()
        actors = Actor.objects.filter(owner = owner)
        documents = Document.objects.filter(owner = owner)
        accesslogs = AccessLog.objects.filter(owner = owner)
        for actor in actors :
            dot.node(actor.type, actor.type)
        for document in documents :
            dot.node(document.type, document.type) 
        for access_log in accesslogs:
            dot.edge(str(access_log.document.id), str(access_log.actor.id))
        


        

        


        

        
        