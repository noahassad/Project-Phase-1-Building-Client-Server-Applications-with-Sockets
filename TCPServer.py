from socket import *

serverPort = 8787
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The TCP server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode().strip()

    # Try to check if input is a number
    if sentence.isdigit() or (sentence.startswith('-') and sentence[1:].isdigit()):
        number = int(sentence)
        if number % 2 == 0:
            reply = f"{number} is even"
        else:
            reply = f"{number} is odd"
    else:
        reply = "Please send a valid integer."

    connectionSocket.send(reply.encode())
    connectionSocket.close()

























