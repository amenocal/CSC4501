#UDPingerClient.py
#Alejandro Menocal - CSC 4501
import random, datetime, time
from socket import *

serverName = '130.39.225.50'
serverPort = 050116

clientSocket = socket(AF_INET, SOCK_DGRAM)

numPings = 10

RTTList = []

counter = 0

def avg(list):
	sum = 0
	for x in list:
		sum += x

	return str(sum/len(list)*1.0)

def max(list):
	max = list[0]
	for x in list[1:]:
		if x > max:
			max = x

	return str(max)

def min(list):
	min = list[0]
	for x in list[1:]:
		if x < min:
			min = x

	return str(min)

def perc(num, whole):
	return float(num)/float(whole) *100


for i in range(1,numPings):
	#for loop
	
	senttime = time.strftime("%H:%M:%S", time.localtime())

	#time = str(datetime.timedelta(seconds=senttime))

	message = 'ping %d %s capitalize this' % (i, senttime)

	intime = time.time()

	clientSocket.sendto(message, (serverName, serverPort))

	clientSocket.settimeout(1)
	try:


		modifiedMessage, serverAddress = clientSocket.recvfrom(050116)

		print modifiedMessage

		RTT = (time.time() - intime)

		#rtttime
		print 'RTT: %s \n\n' % RTT
		RTTList.insert(i, RTT)

		#print 'List %s' % RTTList

	except timeout:
		print 'Request timed out \n\n'
		counter += 1


#close Client Socket
#print 'Counter %d' % counter
print 'Maximum RTT: %s, Minimum RTT: %s, Average RTT: %s' % (max(RTTList), min(RTTList), avg(RTTList))
print 'Packet Loss Rate %d %%' % perc(counter, numPings)
clientSocket.close()