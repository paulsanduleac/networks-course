# Laboratory Work #1

Implemented simple client/server applications that interact on the same machine between two sockets.

Basic features:

1. The server prints debug information about each incoming connection, indicating the remote address.

2. The server implements 4 special commands received from the client:
	
	%Hastalavista - if the server receives this command, it will terminate the connection and shut itself down
	
	%Time - the server will react by sending the client the current time of the system on which the it is running

	random password - the server will react by sending the client a randomly generated password

	%Picsoritdidnthappen - when the server received this command, it will send a link to a picture

3. If the server receives an unknown command - it responds with "Can you elaborate on that?"

4. If the server receives an unknown command that ends with a '?' - it must respond with "42"

Bonus features:
- The server can handle up to 30 incoming connections at the same time. The value can be changed by adjusting the number of threads the server will create.
