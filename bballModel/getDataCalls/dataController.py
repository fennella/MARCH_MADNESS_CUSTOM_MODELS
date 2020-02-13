from . import rankingData, confData, playingData
import time
import random

def getTeamData():

    print("Beginning to get team data")

    teamsDict = rankingData.getTop100IDs()
    print("Successfully gathered top 100 teams")
    time.sleep(1.2)
    teamsDict = confData.getConfData(teamsDict)
    print("Successfully found teams conference/season playing data")
    time.sleep(1.2)
    teamsDict = playingData.getTeamsStats(teamsDict)
    print("Successfully found teams game data")

    lineNums = [num for num in range(1,33)]
    random.shuffle(lineNums)

    for i,team in enumerate(teamsDict):
        teamsDict[team].lineNumber = lineNums[i]
        print(f'{teamsDict[team].name} has line number: {teamsDict[team].lineNumber}')
        teamsDict[team].save()



