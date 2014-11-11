#UDPingerClient.py
#Alejandro Menocal - CSC 4501
#imports
import random, datetime, time
from socket import *

#Server - iP address and Server Port
serverName = ''
serverPort = 050116

#create UDP Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#number of Pings
numPings = 10 

#RTT List in order to calculate max, min and avg
RTTList = []

#counter to know how many requested time out
counter = 0

#Find the Avergae Function
def avg(list):
	sum = 0
	for x in list:
		sum += x

	return str(sum/len(list)*1.0)

#Find the Maximum Function
def max(list):
	max = list[0]
	for x in list[1:]:
		if x > max:
			max = x

	return str(max)

#Find the Minimum Function
def min(list):
	min = list[0]
	for x in list[1:]:
		if x < min:
			min = x

	return str(min)

#Find the Percentange
def perc(num, whole):
	return (float(num)/float(whole))*100

#For loop, since starting at 1, I added 1 for it to send a total of 10 pings.
for seq_num in range(1,numPings+1):

	#Time packet is being sent in Hours, Minutes and Seconds
	senttime = time.strftime("%H:%M:%S", time.localtime())

	#message being sent
	message = 'ping %d %s' % (seq_num, senttime)

	#Message to test to make sure it was capitalizing everything
	#message = 'ping %d %s capitalize this' % (seq_num, senttime)

	#Initial Time Packet is send; Used for RTT
	intime = time.time()

	#sendmessage to Server
	clientSocket.sendto(message, (serverName, serverPort))

	#Set timeout wait to 1 second
	clientSocket.settimeout(1)

	try:
		#receive message
		modifiedMessage, serverAddress = clientSocket.recvfrom(050116)
		
		#print the Modified Message
		print modifiedMessage

		#calculate RTT Time
		RTT = (time.time() - intime)

		print 'RTT: %s \n\n' % RTT
		#insert all the RTT into the List
		RTTList.insert(seq_num, RTT)

	except timeout:
		print 'Request timed out \n\n'
		counter += 1


print 'Maximum RTT: %s, Minimum RTT: %s, Average RTT: %s' % (max(RTTList), min(RTTList), avg(RTTList))
print 'PINGS sent: %d, Packet Loss Rate: %d%%' % (seq_num, perc(counter, numPings))

clientSocket.close()
