import requests

def getConfData(teamsDict):

    teamConfAPI = "https://api.sportradar.us/ncaamb/trial/v7/en/seasons/2019/reg/standings.json?api_key=hk5965y5g3efwk73muqq69xd"
    response = requests.get(teamConfAPI)
    confData = response.json()
    return addAttributesToTeams(confData["conferences"], teamsDict)

def addAttributesToTeams(confData, teamsDict):

    for conf in confData:
        for team in conf["teams"]:
            if team["id"] in teamsDict.keys():
                teamsDict[team["id"]].apd = team["point_diff"]
                teamsDict[team["id"]].wp = team["win_pct"]
                for record in team["records"]:
                    if record["record_type"] == "conference":
                        teamsDict[team["id"]].nonConf = calcNonConfWinPerc(record, team)
                    elif record["record_type"] == "road":
                        teamsDict[team["id"]].awayWP = record["win_pct"]
                    elif record["record_type"] == "last_10":
                        teamsDict[team["id"]].last10 = record["win_pct"]
                    elif record["record_type"] == "top_25":
                        teamsDict[team["id"]].top25 = record["win_pct"]
                
    return teamsDict


def calcNonConfWinPerc(conf, overall):

    totalOutOfConference = (overall["wins"] + overall["losses"]) - (conf["wins"] + conf["losses"])
    totalWinsOutOfConference = overall["wins"] - conf["wins"]

    return round(totalWinsOutOfConference / totalOutOfConference, 2)