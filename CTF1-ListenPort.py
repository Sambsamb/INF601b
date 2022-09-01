# Write a Python script, this script should:
# 1.	connect to this CTF game's ip and on port 20001.
# 2.	after you connect to it, receive the prompt.
# 3.	respond to it to receive your flag.

#!/usr/bin/python              # This is client.py file
import socket                  # Import socket module
s = socket.socket()            # Create a socket object
host = '1.2.3.4'               # Remote Server IP
port = 20001                   # Remote Server Port

"""
print (s)
print (host)
print (port)

exit()
"""

s.connect((host, port))
print (s.recv(1024))
s.send(str.encode('Gimme flag pls'))
print (s.recv(1024))
s.close()                      # Close the socket when done


