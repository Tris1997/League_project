import string
import os
import requests
import json

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
    jsons = requests.get(endpoint, params=payload).json()

    file_exists = os.path.exists('myfile.json')

    if not file_exists:
        to_list = [jsons]
        json_object = json.dumps(to_list, indent=4)

        with open("myfile.json", "a") as file:
            
            file.write(json_object)
    else:
        append_content = []

        with open("myfile.json", "r") as file:
            append_content = json.load(file)

        for id_match in append_content:
            if id == id_match['metadata']['matchId']:
                return jsons

        append_content.append(jsons)
        print(len(append_content))
        json_object = json.dumps(append_content, indent=4)

        with open("myfile.json", "w") as file:
            file.write(json_object)

    return jsons

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