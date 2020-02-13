import requests
import json
import time

def getTeamsStats(teamsDict):

    for key in teamsDict.keys():

        print(f'Getting playing data for {teamsDict[key].name}')
        time.sleep(1.5)
        getTeamStats(teamsDict, key)
        
    
    return teamsDict

    
    
def getTeamStats(teamsDict, key):

    teamStatsAPI = "https://api.sportradar.us/ncaamb/trial/v7/en/seasons/2019/REG/teams/" + key + "/statistics.json?api_key=hk5965y5g3efwk73muqq69xd"

    response = requests.get(teamStatsAPI)
    data = response.json()

    calculateStats(teamsDict, key, data)
    assignStats(teamsDict, key, data)

def calculateStats(teamsDict, key, data):

    POSS = calcPOSS(data)

    calcPACE(teamsDict, key, data, POSS)
    calcORtg(teamsDict, key, data, POSS)
    calcDRtg(teamsDict, key, data, POSS)
    calcNRtg(teamsDict, key, data, POSS)
    calcFTR(teamsDict, key, data)
    calcTS(teamsDict, key, data)
    calcARB(teamsDict, key, data)
    calcBLK(teamsDict, key, data)
    calcEFG(teamsDict, key, data)
    calcTOV(teamsDict, key, data)
    calcORB(teamsDict, key, data)
    calcDefensiveMargin(teamsDict, key, data)
    calcPythWPerc(teamsDict, key, data)

def assignStats(teamsDict, key, data):

    teamsDict[key].ftp = data["own_record"]["total"]["free_throws_pct"]
    teamsDict[key].threepp = data["own_record"]["total"]["three_points_pct"]
    teamsDict[key].fgp = data["own_record"]["total"]["field_goals_pct"]
    teamsDict[key].aa = data["own_record"]["average"]["assists"]
    teamsDict[key].avgs = data["own_record"]["average"]["steals"]
    teamsDict[key].afbp = data["own_record"]["average"]["fast_break_pts"]
    teamsDict[key].ascp = data["own_record"]["average"]["second_chance_pts"]
    teamsDict[key].aps = data["own_record"]["average"]["points"]
    teamsDict[key].apa = data["opponents"]["average"]["points"]
    teamsDict[key].aorb = data["own_record"]["average"]["off_rebounds"]
    teamsDict[key].ab = data["own_record"]["average"]["blocks"]
    teamsDict[key].at = data["own_record"]["average"]["turnovers"]
    teamsDict[key].apip = data["own_record"]["average"]["points_in_paint"]

# 100 * ((POINTS - Opponent Points) / POSS)
def calcNRtg(teamsDict, key, data, POSS):

    POINTS = data["own_record"]["total"]["points"]
    OPOINTS = data["opponents"]["total"]["points"]

    teamsDict[key].nrtg = 100 * ((POINTS - OPOINTS) / POSS)

# POINTS^16.5 / (POINTS^16.5 + Opponent Points^16.5)
def calcPythWPerc(teamsDict, key, data):

    POINTS = data["own_record"]["total"]["points"]
    OPOINTS = data["opponents"]["total"]["points"]

    teamsDict[key].PythW = POINTS**16.5 / (POINTS**16.5 + OPOINTS**16.5)

# 100 * (Opponent Points / POSS)
def calcDRtg(teamsDict, key, data, POSS):

    OPTS = data["opponents"]["total"]["points"]
    
    teamsDict[key].drtg = 100 * (OPTS / POSS)

# ORB / (ORB + Opponent Defensive Rebounds)
def calcORB(teamsDict, key, data):

    ORBS = data["own_record"]["total"]["offensive_rebounds"]
    ODRBS = data["opponents"]["total"]["defensive_rebounds"]

    teamsDict[key].orb = ORBS / (ORBS + ODRBS)

# 100 * Turnovers / (FGA + 0.475 * FTA + Turnovers)
def calcTOV(teamsDict, key, data):

    TOVS = data["own_record"]["total"]["turnovers"]
    FGA = data["own_record"]["total"]["field_goals_att"]
    FTA = data["own_record"]["total"]["free_throws_att"]

    teamsDict[key].tovr = 100 * TOVS / (FGA + 0.475 * FTA + TOVS)


# (FG + 0.5 * 3P) / FGA
def calcEFG(teamsDict, key, data):

    FG = data["own_record"]["total"]["field_goals_made"]
    THREES = data["own_record"]["total"]["three_points_made"]
    FGA = data["own_record"]["total"]["field_goals_att"]

    teamsDict[key].efg = (FG + 0.5 * THREES) / FGA

# Total Blocks / Opponent FGA
def calcBLK(teamsDict, key, data):

    TBLK = data["own_record"]["total"]["blocks"]
    OFGA = data["opponents"]["total"]["field_goals_att"]

    teamsDict[key].blkp = TBLK / OFGA

# Points Allowed / (Points Allowed + Points Scored)
def calcDefensiveMargin(teamsDict, key, data):

    pointsScored = data["own_record"]["total"]["points"]
    pointsAllowed = data["opponents"]["total"]["points"]

    teamsDict[key].dm = pointsAllowed / (pointsAllowed + pointsScored)

# 100 * (Points / POSS)
def calcORtg(teamsDict, key, data, POSS):

    POINTS = data["own_record"]["total"]["points"]

    teamsDict[key].ortg = 100 * (POINTS / POSS)

# Points / (2 * (FGA + 0.475 * FTA))
def calcTS(teamsDict, key, data):

    POINTS = data["own_record"]["total"]["points"]
    FGA = data["own_record"]["total"]["field_goals_att"]
    FTA = data["own_record"]["total"]["free_throws_att"]

    teamsDict[key].ts = POINTS / (2 * (FGA + 0.475 * FTA))

# Free throw attempts / field goal attempts
def calcFTR(teamsDict, key, data):

    FTA = data["own_record"]["total"]["free_throws_att"]
    FGA = data["own_record"]["total"]["field_goals_att"]

    teamsDict[key].ftr = FTA / FGA 


# (Total Rebounds - Opponent Total Rebounds) / Total Games
def calcARB(teamsDict, key, data):

    TRB = data["own_record"]["total"]["rebounds"]
    OTRB = data["opponents"]["total"]["rebounds"]
    GP = data["own_record"]["total"]["games_played"]

    teamsDict[key].erb = (TRB - OTRB) / GP

# 40 * (POSS / (0.2 * Minutes Played))
def calcPACE(teamsDict, key, data, POSS):

    PACE = 40 * (POSS / (0.2 * data["own_record"]["total"]["minutes"]))
    teamsDict[key].pace = PACE

# 0.5 * (FGA + 0.475 * FTA - ORB + TOV) + 0.5 * (OFGA + 0.475 * OFTA - OORB + OTOV)
def calcPOSS(data):

    FGA = data["own_record"]["total"]["field_goals_att"]
    FTA = data["own_record"]["total"]["free_throws_att"]
    ORB = data["own_record"]["total"]["offensive_rebounds"]
    TOV = data["own_record"]["total"]["turnovers"]

    OFGA = data["opponents"]["total"]["field_goals_att"]
    OFTA = data["opponents"]["total"]["free_throws_att"]
    OORB = data["opponents"]["total"]["offensive_rebounds"]
    OTOV = data["opponents"]["total"]["turnovers"]

    return round(0.5 * (FGA + 0.475 * FTA - ORB + TOV) + 0.5 * (OFGA + 0.475 * OFTA - OORB + OTOV),4)


