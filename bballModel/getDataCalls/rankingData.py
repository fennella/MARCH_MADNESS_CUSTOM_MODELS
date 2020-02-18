import requests
import json
from ..models import Team

def getTop100IDs():

    rankingAPI = "https://api.sportradar.us/ncaamb/trial/v7/en/rpi/2019/rankings.json?api_key=hk5965y5g3efwk73muqq69xd"

    response = requests.get(rankingAPI)
    data = response.json()
    return createDict(data["rankings"][:64])
    
def createDict(allData):

    myDict = {}

    for teamData in allData:

        team = Team()
        team.teamID = teamData["id"]
        team.name = teamData["market"]
        team.owp = teamData["owp"]
        team.oowp = teamData["oowp"]
        team.awp = teamData["awp"]
        team.SOS = teamData["sos"]
        team.RPI = teamData["rpi"]
        myDict[teamData["id"]] = team
    
    return myDict