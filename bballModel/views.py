from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getDataCalls import dataController
import json
import operator
from .models import Team
import random

def index(request):

    #dataController.getTeamData()

    return render(request, 'bballModel/index.html')


def calcModel_view(request):

    weightsDict = json.loads(request.GET.get('weightsDict'))
    teams = Team.objects.order_by('lineNumber')
    teamScoreDict = {}

    # Init dictionary to hold each teams score
    for team in teams:
        teamScoreDict[team.teamID] = {"name":team.name, "score":0}

    # Sum team score for each weight specified
    for weight in weightsDict:
        if int(weightsDict[weight]["weight"]) > 0:
            teamScoreDict = addWeightScore(teamScoreDict, teams, int(weightsDict[weight]["weight"]), weightsDict[weight]["stat"])

    results = determineWinners(teams, teamScoreDict) 
    
    return JsonResponse(results, safe=False)

def addWeightScore(teamScoreDict, teams, weight, stat):

    if stat == "tovr" or stat == "apa" or stat == "at":
        orderedTeams = sorted(teams, key=operator.attrgetter(stat), reverse=True)
    else:
        orderedTeams = sorted(teams, key=operator.attrgetter(stat))

    
    for i,team in enumerate(orderedTeams):
        
        weightScore = (i / (len(orderedTeams) - 1)) * weight
        teamScoreDict[team.teamID]["score"] += weightScore
    
    return teamScoreDict

def determineWinners(teams, teamScoreDict):

    results = [[]]

    for team in teams:
        results[0].append(teamScoreDict[team.teamID]) 

    return winnerHelper(results, 1)


def winnerHelper(results, roundNum):

    if roundNum == 7: return results

    results.append([])

    for i,team in enumerate(results[roundNum - 1]):
        if i % 2 == 0: continue

        if team["score"] > results[roundNum - 1][i - 1]["score"]:
            results[roundNum].append(team)
        elif team["score"] < results[roundNum - 1][i - 1]["score"]:
            results[roundNum].append(results[roundNum - 1][i - 1])

        # Somehow a tie...very low probability
        # Randomly choose winner
        else:
            randNum = random.randint(0,1)
            if randNum == 0: results[roundNum].append(team)
            else: results[roundNum].append(results[roundNum - 1][i - 1])


    return winnerHelper(results, roundNum + 1)






