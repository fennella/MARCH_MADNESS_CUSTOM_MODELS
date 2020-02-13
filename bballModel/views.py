from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getDataCalls import dataController
import json

def index(request):

    #dataController.getTeamData()

    return render(request, 'bballModel/index.html')


def calcModel_view(request):

    print("Calculating Model")
    weightsDict = json.loads(request.GET.get('weightsDict'))
    
    return JsonResponse({'message':'received'})
