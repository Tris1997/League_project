import requests
import os
import datetime
from endpoint_functions import *
import plotly.express as px
import pandas as pd
# Tristan's
#{"summonerID":"GtuLgsQ0rBzcKnjEagd6vZhT3YMvKAwW5Lwy1khpK9eUWYw",
# "accountId":"zSpDaO6Abvqdya5zpt5CcVwsGhbDbFdjkL_h7e195wIHsA",
# "puuid":"tVek217N2bNcy-YFK2uIuXSe4zM1UEq1YhnDApul37etd3rImE3a85WnewqoEdZZUpGxzNJxpXeBsA",
# "name":"Dollheart",
# "profileIconId":1114,"revisionDate":1662768219129,"summonerLevel":794}

# Faker's
# 'summonerId': 'fjkeDtrlsQJ1lWfdp_eqGBfN0OdPunwLKzxblNhdDIMAfA', 
# 'accountId': 'O39zP8xO-OjiWItN0STjSwex6h4y8VglbnP5mH1nPYPP',
# 'puuid': 'CDGxXdP1ELtI95zs3v5NgwcAej-q7IUA3fVLvn7Kt_1UlSFej6rsLaJqdRi7HQ7H2w43BIp2j1OvKw',
# 'name': 'Hide on
# bush', 'profileIconId': 6, 'revisionDate': 1662837244000, 'summonerLevel': 600


# 'id': 'mvSNTltcTWbqxizkIua8hvS3Yxa4Odu7rbc__T6uFwQlXEg',
# 'accountId': 'TvEf_cKjmeInXOD3PEqXJRJJYQXU5ti4nGHqoSAurd2Q9d8',
# 'puuid': 'SLnT0cSY0o58hrEXwnl-Fe-DfxsVC8LDFdPlkK0aUJlYDY1PETWMQYeAZ_5hVUIl2W75N9xikRFf3Q', 
# 'name': '냥똥벌레',
# 'profileIconId': 4022, 
# 'revisionDate': 1662793539886, 
# 'summonerLevel': 458

"""**Endpoints**"""
# /lol/league-exp/v4/entries/{queue}/{tier}/{division}
# /lol/league/v4/entries/by-summoner/{encryptedSummonerId}    `
# /lol/league/v4/leagues/{leagueId}
# /lol/summoner/v4/summoners/by-name/{summonerName}
# /lol/match/v5/matches/{matchId}
# /lol/match/v5/matches/by-puuid/{puuid}/ids
if __name__ == "__main__":
    payload = {'api_key': os.getenv('API_KEY'),'count': 40 }

    player = summonerName("Dollheart")
    print(player)

    na_matches_list = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids'.format(player["puuid"]), \
        params=payload).json()


    matches_won = {}
    for match in na_matches_list:
        na_url = matchID(match)
        print(na_url)
        unix_timestamp = int(na_url["info"]["gameEndTimestamp"])

        unix_second = int(unix_timestamp / 1000)

        match_date = datetime.datetime.fromtimestamp(unix_second).date()
        win_clause = na_url["info"]["participants"][0]["win"]
        
        if match_date not in matches_won.keys() and win_clause:
            matches_won[match_date] = {}
            matches_won[match_date]["win"] = 0

            matches_won[match_date]["lose"] = 0

            matches_won[match_date]["win"] += 1
        elif win_clause:
            matches_won[match_date]["win"] += 1
        elif match_date not in matches_won.keys() and not win_clause:
            matches_won[match_date] = {}
            matches_won[match_date]["win"] = 0

            matches_won[match_date]["lose"] = 0
            matches_won[match_date]["lose"] += 1
        else:
            matches_won[match_date]["lose"] += 1

    to_graph = {
        "Date": [],
        "Win":[],
        "Lost":[]
    }

    for value in matches_won:
        to_graph["Date"].append(value)
        to_graph["Win"].append(matches_won[value]["win"])
        to_graph["Lost"].append(matches_won[value]["lose"])
    
    df = pd.DataFrame(
        to_graph
    )
    
    print(df)

    fig = px.bar(df,x=to_graph["Date"],y=[to_graph["Win"],to_graph["Lost"]])
    fig.show()

    
