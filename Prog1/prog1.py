# Alejandro Menocal
# Oct 1, 2014
# CSC 4501 - Prog 1


#import socket module
from socket import *

serverPort = 50116
serverName = '167.96.50.29'
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket

serverSocket.bind ((serverName, serverPort))
serverSocket.listen(1)


while True:
		#Establish connection
		print 'Ready to serve...'

		connectionSocket, addr = serverSocket.accept()
		

		try:
			message = connectionSocket.recv(50116)

			filename = message.split()[1]

			f = open(filename[1:])

			outputdata = f.read()

			f.close()

			#Send one HTTP header line into socket
			header = ('HTTP/1.1 200 OK \r\n Content-Type: text/html\r\n\r\n')
			
			connectionSocket.send(header)
			

			#Send the content of the requested file to the client

			for i in range(0, len(outputdata)):

				connectionSocket.send(outputdata[i])

			#print 'Sending the file'	
			connectionSocket.close()

		except IOError:
			
			#Send response message for file not found
			print 'You are in the error code'

			#Fill in start
			connectionSocket.send('404 Not found')

			#Close client socket
			connectionSocket.close()