"""
Improve your Python script one last time, this new script should:
1. connect to this CTF games' ip and on port 20003.
2. after you connect to it, receive the prompt.
3. respond to it to receive your flag.
"""

# !/usr/bin/python                  # This is client.py file
import socket                       # Import socket module
s = socket.socket()                 # Create a socket object
host = '1.2.3.4'                    # Remote Server IP
port = 20003                        # Remote Server Port
s.connect((host, port))
print(s.recv(1024).decode())        # Calc the sum of the given numbers in 3 seconds, 5 pairs, "begin" to continue
s.send(str.encode('begin'))
for x in range(0, 5):
    myvar1 = s.recv(1024).decode()  # The numbers are: 4083 and 2224
    print(myvar1)
    z = int(myvar1[17:21]) + int(myvar1[26:30])
    print('The total is:', z)
    s.send(str.encode(str(z)))
print(s.recv(1024).decode())
s.close()                           # Close the socket when done
