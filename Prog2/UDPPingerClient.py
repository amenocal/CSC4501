#UDPingerClient.py
#Alejandro Menocal - CSC 4501
import random, datetime, time
from socket import *

#serverName = ''
serverPort = 050116

clientSocket = socket(AF_INET, SOCK_DGRAM)

numPings = 10

for i in range(1,numPings):
	#for loop
	
	senttime = time.localtime()

	time = str(datetime.timedelta(seconds=senttime))

	message = 'Ping %d %s' % (i, time)

	clientSocket.sendto(message, (serverName, serverPort))

	clientSocket.settimeout(1)
	try:


		modifiedMessage, serverAddress = clientSocket.recvfrom(050116)

		print modifiedMessage

		#rtttime


	except timeout:
		print 'Request timed out \n\n'

#close Client Socket
clientSocket.close()