import threading, sys
from socket import * 
from datetime import datetime
import random, string

listeningSocket = socket()
listeningSocket.bind( ("127.0.0.1", 6000) )
port=listeningSocket.getsockname()
print "\n" + "Socket bind succesful on " + gethostname() + ":" + str(port) + "\n"

def handleconnection(socket):
	while 1:
	    data = socket.recv(1024)
	    print data
	    if "exit" in data: 
	    	break
	    elif "%Hastalavista" in data:
			break
	    elif "%Picsoritdidnthappen" in data:
	    	data="http://info.railean.net/images/b/bd/Terminator2.jpg"
	    elif "%Time" in data:
	    	time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	    	data=time
	    elif "random password" in data:
	    	data = ''.join(random.choice(string.ascii_lowercase+ string.ascii_uppercase + string.digits) for _ in range(10))
	    elif "?" in data:
	    	data=str(42)
	    else:
	    	data="Can you elaborate on that?"
	    data=data+"\n"
	    socket.sendall(data)

def runsocket():
		#accept an incoming connection
		newAllocatedSocket, address = listeningSocket.accept()
		print "Connection established:" + str(address)
		newAllocatedSocket.send("Hello stranger. \n") #send a message to the client
		handleconnection(newAllocatedSocket)
		newAllocatedSocket.close()

#make it listen
listeningSocket.listen(5)

for i in range(30):
	threading.Thread(target=runsocket).start()
print "Ready to accept up to 30 incoming connections."
#close everything and get outta here
if KeyboardInterrupt: sys.exit()
listeningSocket.close()