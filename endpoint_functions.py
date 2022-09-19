import string
import os
import requests

"""Endpoint Functions"""

payload = {'api_key': os.getenv('API_KEY')}


def summonerID(id):
    encryptedSummonerId = id
    endpoint = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}'.format(encryptedSummonerId)
    json = requests.get(endpoint, params=payload).json()
    return json

def summonerName(name):
    summoner_name = name
    endpoint = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}'.format(summoner_name)
    json = requests.get(endpoint, params=payload).json()
    return json

def matchID(id):
    match_id = id
    endpoint = 'https://americas.api.riotgames.com/lol/match/v5/matches/{}'.format(match_id)
    json = requests.get(endpoint, params=payload).json()
    return json

# /lol/match/v5/matches/by-puuid/{puuid}/ids

def matchList(id):
    puuid = id
    endpoint = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids'.format(puuid)
    json = requests.get(endpoint, params=payload)
    return json
    
    
"""tests"""
if __name__ == "__main__":
    result = summonerID("GtuLgsQ0rBzcKnjEagd6vZhT3YMvKAwW5Lwy1khpK9eUWYw")
    print(result.json())

    result2 = summonerName('Dollheart')
    print(result2.json())

    result3 = matchList('tVek217N2bNcy-YFK2uIuXSe4zM1UEq1YhnDApul37etd3rImE3a85WnewqoEdZZUpGxzNJxpXeBsA')
    print(result3.json())

    result4 = matchID('NA1_4436996610')
    print(result4.json())