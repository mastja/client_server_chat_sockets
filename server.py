# Project 4 - Server and Client Chat Program - server file
# Programmer - Jacob Mast
# Date 8/5/2020
# Description - Simple client-server program using python sockets. Program emulates a simple chat server. 
# source. 1 - https://www.binarytides.com/python-socket-programming-tutorial/
# source. 2 - https://realpython.com/python-sockets/#running-the-echo-client-and-server
# source. 3 - https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# source. 4 - https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python

import socket	#for sockets
import sys	#for exit

#source for setting up the socket - https://www.binarytides.com/python-socket-programming-tutorial/
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888        # Port to listen on (non-privileged ports are > 1023)
name = "Server"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
	s.bind(('', PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

#wait to accept a connection - blocking call
conn, addr = s.accept()

print 'Connected with ' + addr[0] + ':' + str(addr[1])

#source for code and loop below: https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
s_name = conn.recv(1024)
s_name = s_name.decode()
print '\n' + s_name + ' has connected to the chat room\nEnter "/q" to quit\n'
conn.send(name.encode())

#quit message from client, for use in if statement below
client_quit = 'Left chat room!'

#send and receive messages with the client in loop until a quit message is either sent or received
while True:
    message = raw_input(str('Me : '))
    message = message.strip()	#source: https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python
    if message == '/q':
        message = 'Left chat room!'
        conn.send(message.encode())
        print '\n'
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print s_name + ' : ' + message
    if message == client_quit:
        break

#close the connection
conn.close()
print 'client disconnected\n'

s.close()
print 'program closing'