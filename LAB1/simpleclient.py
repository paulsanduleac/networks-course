from socket import * 
from time import sleep
socket = socket()
socket.bind( ("127.0.0.1", 0) )
port=socket.getsockname()
print "\n" + "Socket bind succesful on " + gethostname() + ":" + str(port) + "\n"

socket.connect(("127.0.0.1",6000))

msg=["%Picsoritdidnthappen","%Time","Are you there?","random password please","%Hastalavista"]

data=socket.recv(1024)
print "INCOMING: " + data
for i in range(5):
	print "SENDING: " + msg[i]
	socket.sendall(msg[i])
	data=socket.recv(1024)
	#while (data):
    #    print "Receiving..."
    #    f.write(data)
    #    data = socket.recv(1024)
	print "RESPONSE: " + data

while 1:
	data=socket.recv(1024)
	if data=='': break #detect if connection closed

socket.close()
