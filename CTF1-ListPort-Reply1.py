"""
Improve your Python script, this new script should:
1. connect to this CTF games' ip and on port 20002.
2. after you connect to it, receive the prompt.
3. respond to it to receive your flag.
"""

# !/usr/bin/python           # This is client.py file
import socket                # Import socket module
s = socket.socket()          # Create a socket object
host = '1.2.3.4'             # Remote Server IP
port = 20002                 # Remote Server Port
s.connect((host, port))
myvar1 = s.recv(1024)
myvar2 = myvar1.decode()
print(myvar2)                # Send me back this string: 12345678, I will reply with the flag
myvar3 = myvar2[26:34]
print('Sending:', myvar3)    # 12345678
s.send(str.encode(myvar3))
print(s.recv(1024).decode())
s.close()                    # Close the socket when done
