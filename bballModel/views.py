from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getDataCalls import dataController
import json
import operator
from .models import Team

def index(request):

    #dataController.getTeamData()

    return render(request, 'bballModel/index.html')


def calcModel_view(request):

    weightsDict = json.loads(request.GET.get('weightsDict'))
    teams = Team.objects.order_by('lineNumber')
    teamScoreDict = {}

    # Init dictionary to hold each teams score
    for team in teams:
        teamScoreDict[team.teamID] = 0

    for weight in weightsDict:
        if int(weightsDict[weight]["weight"]) > 0:
            teamScoreDict = addWeightScore(teamScoreDict, teams, int(weightsDict[weight]["weight"]), weightsDict[weight]["stat"])
            
    return JsonResponse({'message':'received'})

def addWeightScore(teamScoreDict, teams, weight, stat):

    orderedTeams = sorted(teams, key=operator.attrgetter(stat))
    
    for i,team in enumerate(orderedTeams):
        
        weightScore = (i / len(orderedTeams)) * weight
        teamScoreDict[team.teamID] += weightScore
    
    return teamScoreDict






