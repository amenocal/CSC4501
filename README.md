##Programs done for Computer Networking at LSU

##Prog 1: Web Server Socket Programming

Developed a Web server that handled one HTTP request at a time. It accepts and parsed the HTTP request, gets the requested file from the server's file system, creates an HTTP response message which is the file, and sends the response direclty to client.

Running: Put a file(in my case .html file) in same directory. Determine the IP address of host where the server is running. From another PC type in host's IP Address into the browser plus the corresponding URL.

Example: http://123.456.789.01/HelloWorld.html 

##Prog 2: Socket UDP Programming

Sends and receives a datagram packets using UDP sockets. We will be using a similar functionality used by ping programs. This ping protocol will allow a client machine to send packets of data to a remote machine, and have the remote machine return the data back to the client withous changing it.
