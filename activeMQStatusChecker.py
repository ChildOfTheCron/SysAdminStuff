#!/usr/bin/python3.5
 
import requests
import json
import time
import configparser
import io

class QueueDataStorage(object):
	def __init__(self, queueData, consumerData):
		self.queueData = queueData
		self.consumerData = consumerData

class QueueParser(object):
	def __init__(self, queueURL, user, passwd):
		self.queueURL = queueURL
		self.user = user
		self.passwd = passwd

	def getData(self): 

		#config = configparser.RawConfigParser(allow_no_value=False)
		#config.read("queueConfig.cfg")
		
		#print(config.items("Queue"))
		rawJsonData = requests.get(self.queueURL, auth=(self.user, self.passwd))
	
		firstVal = rawJsonData.json()
		subDict = firstVal['value']

		newJson = json.dumps(subDict, sort_keys=True, indent=4, separators=(',', ': ')) 
		#print(json.dumps(subDict, sort_keys=True, indent=4, separators=(',', ': ')))

		queueJson = json.loads(newJson)
	
		#print("Queue Size: " + str(queueJson["QueueSize"]))
		#print("Consumer Count: " + str(queueJson["ConsumerCount"]))

		queueData = QueueDataStorage(queueJson["QueueSize"], queueJson["ConsumerCount"])	
		#queueSize = queueJson["QueueSize"]
		return queueData

if __name__ == "__main__":
	
	config = configparser.RawConfigParser(allow_no_value=False)
	config.read("queueConfig.cfg")
	queueItems = config.items("Queue")
	queueUser = config.get("AuthUser", "User") 
	queuePass = config.get("AuthUser", "Pass")

	oldObjectPool = {}
	newObjectPool = {}	

	for x in queueItems:
		tmpParser = QueueParser(x[1], queueUser, queuePass)
		tmpParserData = tmpParser.getData()
		tmpID = x[1]
		oldObjectPool = {tmpID : tmpParserData}
		#print(x[1])
		#print(tmpParserData.queueData)
		#print(tmpParserData.consumerData)
		print(oldObjectPool)
	
	time.sleep(60)
	
	for x in queueItems:
		#newRun = QueueParser.getQueueSize(queueItems)
		tmpParser = QueueParser(x[1], queueUser, queuePass)
		tmpParserData = tmpParser.getData()
		tmpID = x[1]
		newObjectPool = {tmpID : tmpParserData}
		print(newObjectPool)

	for key in oldObjectPool:
		if (key in newObjectPool):
			if (oldObjectPool[key].consumerData == 0 or newObjectPool[key].consumerData == 0):
				print("DANGER WILL ROBINSON! THE CONSUMERS ARE DEAD! RUN!")
			if (oldObjectPool[key].queueData < newObjectPool[key].queueData):
				print("DANGER WILL ROBINSON! QUEUE SIZE LARGER THAN BEFORE!")



