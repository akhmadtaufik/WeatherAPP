import requests
import json
from datetime import datetime, timedelta
from GetCitiesID import getCityIDByCountry, saveToCsv

# Read PWD
f = open("config.txt", "r")
lines = f.readlines()
myPass = lines[0].strip()
myAPI  = lines[1]
f.close()

# Getting API Data
url = 'http://api.openweathermap.org/data/2.5/group?appid={}&id={}&lang=id'

listID = ['1650357','1650332']
#print(*listID, sep=',')

resp = requests.get(url.format(myAPI, ','.join(listID)))
rawData = resp.json()
print(rawData)