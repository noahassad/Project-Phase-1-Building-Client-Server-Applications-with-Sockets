from socket import *

serverName = '10.186.234.32'   
serverPort = 8787             
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

number = input('Enter a number: ')
clientSocket.send(number.encode())

reply = clientSocket.recv(1024)
print('From Server:', reply.decode())

clientSocket.close()
