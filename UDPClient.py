from socket import *

serverName = '10.186.234.32'   
serverPort = 7171             
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))

number = input('Enter a number: ')
clientSocket.send(number.encode())

reply = clientSocket.recv(1024)
print('From Server:', reply.decode())

clientSocket.close()
