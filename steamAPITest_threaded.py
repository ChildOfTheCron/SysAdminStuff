#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 
import sys
import requests
import time
import datetime
import threading
import time

sqlContentTest = []

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, val):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.val = val
   def run(self):
      print ("Starting " + self.name)
      getDisc(self.val)
      print ("Exiting " + self.name)

def getAppIdList():
   
    req4 = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v2')
    
    firstVal = req4.json()
    subDict = firstVal['applist']
    secondVal = subDict['apps']

    return secondVal

def lookUpDiscount(sndVal):

    hackyCount = 0
    for val in sndVal:

        if hackyCount < 10:
            hackyCount = hackyCount + 1
            thread = myThread(hackyCount, "thread-"+str(hackyCount),val)
            thread.start()
            thread.join()
        else:
            break;

def getDisc(val):

    s = requests.Session() # Remove this??

    jsonAppID = val['appid']
    appreq    = s.get('https://store.steampowered.com/api/appdetails/?appids=' + str(val['appid']) + '&cc=EE&l=english&v=1')
    appfirstVal = appreq.json()
    tmpdisc = '0%'

    try:
        appsubDict = appfirstVal[str(val['appid'])]
        appsecondVal = appsubDict['data']
        appthirdVal = appsecondVal['package_groups']
        appfourthVal = appthirdVal[0]
        appfithVal = appfourthVal['subs']
        appsixVal = appfithVal[0]
        appseventhVal = appsixVal['percent_savings_text']
        tmpdisc = appseventhVal
        print(appseventhVal)
        #break <-- Debug stuff, uncomment this to jump out when you hit the first discount
    except:
        print("Unknown json found, will set to 0%")

    if (tmpdisc == ""):
        tmpdisc = "0%"

    sqlContentTest.append([val['appid'], val['name'], tmpdisc])

# Grab a list of all steam app id's using the web API, not sure if this is returning them all
# but I got no control over that
#req4    = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v2')

#Note start time so I can see how long this takes
print("Probed run start on: ", datetime.datetime.now().strftime("%d/%m/%y::%H-%M-%S"))

appList = getAppIdList()
lookUpDiscount(appList)

# Set up some variables we'll need
#sqlContent = []
#firstVal = req4.json()
#subDict = firstVal['applist']
#secondVal = subDict['apps']

# The docs say that reusing the same HTTP connection will use the underlying TCP connection
# resulting in faster performance but my code runs slower when I use a session other just spamming GETs
# Not sure what the best solution is, also dont wanna spam steam with 80K get requests whenever I run this...
#s = requests.Session()

#hackyCount = 0

# For each AppID that's been returned we wanna parse the json and grab the discount code
# This is a list in a list in a list in a list in a list .... you get the point, terrible code that needs to be cleant up
#for val in secondVal:
#    
#    if hackyCount > 40:
#        break;
#    else:
#        hackyCount = hackyCount + 1
#
#    jsonAppID = val['appid']        
#    appreq    = s.get('https://store.steampowered.com/api/appdetails/?appids=' + str(val['appid']) + '&cc=EE&l=english&v=1')
#    appfirstVal = appreq.json()   
#    tmpdisc = '0%'
#
#    try:
#        appsubDict = appfirstVal[str(val['appid'])]
#        appsecondVal = appsubDict['data']
#        appthirdVal = appsecondVal['package_groups']
#        appfourthVal = appthirdVal[0]
#        appfithVal = appfourthVal['subs']
#        appsixVal = appfithVal[0]
#        appseventhVal = appsixVal['percent_savings_text']
#        tmpdisc = appseventhVal
#        print(appseventhVal)
#        #break <-- Debug stuff, uncomment this to jump out when you hit the first discount
#    except:
#        print("Unknown json found, will set to 0%")
#
#    if (tmpdisc == ""):
#        tmpdisc = "0%"
#
#    sqlContent.append([val['appid'], val['name'], tmpdisc])    
#
#Print end run timestamp and create .sql file for use by my PGDB
print("Probed run end on: ", datetime.datetime.now().strftime("%d/%m/%y::%H-%M-%S"))

file = open("appidlist.sql", "w")
file.write("INSERT INTO appIdTable ( appId, productName, discount ) VALUES \n")
for key in sqlContentTest:
    # Debug stuff
    #print("Key:" + str(key['appid'])  + "\n")
    #print("Name:" + key['name'] + "\n")
    
    # Don't print a comma on the last line of the SQL
    if set(key) == set(sqlContentTest[-1]):
        file.write("(" + str(key[0]) + "," + "'" + key[1] + "'" + "," + "'" + key[2] + "'" + ")" + "\n")
    else:    
        file.write("(" + str(key[0]) + "," + "'" + key[1] + "'" + "," + "'" + key[2] + "'" + ")" + "," + "\n")
file.close()    
