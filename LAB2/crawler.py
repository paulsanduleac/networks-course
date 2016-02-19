from socket import *
from fileinput import input
socket=socket()

def DownloadFile(address,path,filename):
	message = ('GET /' + path + ' HTTP/1.0\n\n')
	socket.connect((address, 80))
	print address
	print message
	socket.send(message)
	f = open(filename, 'w')
	while True:
		resp = socket.recv(1024)
		if resp == "":
			print "Writing to file completed. \n"
			break
		f.write(resp)
	f.close()
	try:
		socket.shutdown(SHUT_RDWR)
		socket.close()
	except error:
		print "Socket closed."

def ProcessHeaders(rawfile, processedfile):
	f1=open(rawfile, 'r')
	f2=open(processedfile, 'w')
	i=0
	for line in f1:
		if len(line)<=2:
			i=1
		elif i==1:
			f2.write(line)
	f1.close()
	f2.close()
	print rawfile+" processed, new file saved to "+processedfile




DownloadFile('www.nytimes.com', '', 'rawindex.html')

ProcessHeaders('rawindex.html','index.html')
