# Project 4 - Server and Client Chat Program - Client file
# Programmer - Jacob Mast
# Date 8/5/2020
# Description - Simple client-server program using python sockets. Program emulates a simple chat client. 
# source. 1 - https://www.binarytides.com/python-socket-programming-tutorial/
# source. 2 - https://realpython.com/python-sockets/#running-the-echo-client-and-server
# source. 3 - https://www.geeksforgeeks.org/socket-programming-python/#:~:text=One%20socket(node)%20listens%20on,real%20backbones%20behind%20web%20browsing.
# source. 4 - https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
# source. 5 - https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python

import socket	#for sockets

#source for setting up the socket - https://www.geeksforgeeks.org/socket-programming-python/#:~:text=One%20socket(node)%20listens%20on,real%20backbones%20behind%20web%20browsing.
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
  
# Define the port on which you want to connect 
port = 8888    
name = 'Client'            
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

#source for code and loop below: https://www.biob.in/2018/04/simple-server-and-client-chat-using.html
#send name first, receive name from server
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print '\n' + s_name + ' has joined the chat room \nEnter "/q" to exit chat room \n'

#quit message from server, for use in if statement below
server_quit = 'Left chat room!'

#send and receive messages with the server in loop until a quit message is either sent or received
while True:
    message = s.recv(1024)
    message = message.decode()
    print s_name + ' : ' + message
    if message == server_quit:
        break
    message = raw_input(str('Me : '))
    message = message.strip()	#source: https://stackoverflow.com/questions/45936401/string-comparison-does-not-work-in-python
    if message == '/q':
        message = 'Left chat room!'
        s.send(message.encode())
        print '\n'
        break
    s.send(message.encode()) 

# close the connection 
s.close()
print 'program closing'