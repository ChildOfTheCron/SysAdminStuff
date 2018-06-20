#!/usr/bin/python3.5
 
import sys
import requests
import time
import datetime

args = {'appid': '578080'}

req = requests.get('https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/', params=args)

print(req.status_code)
print(req.text)
print("Probed on: ", datetime.datetime.now().strftime("%d/%m/%y::%H-%M-%S"))

