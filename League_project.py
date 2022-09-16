import requests
import os 
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
payload = {'api_key': os.getenv('API_KEY')}

na_url = requests.get('https://na1.api.riotgames.com/lol/status/v4/platform-data',params=payload)
print(na_url.json())

