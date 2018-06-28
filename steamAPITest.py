#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 
import sys
import requests
import time
import datetime

args    = {'appid': '578080'}
args2   = {'gameid': '578080'}

req     = requests.get('https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/', params=args)
req2    = requests.get('https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/', params=args2)
req3    = requests.get('https://store.steampowered.com/api/appdetails/?appids=730&cc=EE&l=english&v=1')
req4    = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v2')

print(req.status_code)
#print(req.text)
print("Probed on: ", datetime.datetime.now().strftime("%d/%m/%y::%H-%M-%S"))
#print(req2.status_code)
#print(req2.text)
#print(req3.status_code)
#print(req3.text)

#print(req4.status_code)
#file = open("apilist.json","w") 
#file.write(req4.json()) 
#file.close() 

#req4.encoding = 'UTF-8'
firstVal = req4.json()
subDict = firstVal['applist']
secondVal = subDict['apps']

file = open("appidlist.sql", "w")
file.write("INSERT INTO appIdTable ( appId, productName ) VALUES \n")
for key in secondVal:
    #print("Key:" + str(key['appid'])  + "\n")
    #print("Name:" + key['name'] + "\n")
    file.write("(" + str(key['appid']) + "," + key['name']  + ")" + "," + "\n")
file.close()    
